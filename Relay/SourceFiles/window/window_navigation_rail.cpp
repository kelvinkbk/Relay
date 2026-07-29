#include "window/window_navigation_rail.h"
#include "window/window_session_controller.h"
#include "main/main_session.h"
#include "main/main_account.h"
#include "data/data_session.h"
#include "data/data_user.h"
#include "data/data_folder.h"
#include "boxes/peer_list_controllers.h"
#include "calls/calls_box_controller.h"
#include "ui/widgets/buttons.h"
#include "ui/unread_badge.h"
#include "styles/style_window.h"
#include "styles/style_dialogs.h"
#include "styles/style_chat.h" // popupMenuExpandedSeparator
#include "styles/style_menu_icons.h"
#include "ui/widgets/popup_menu.h"
#include "ui/widgets/menu/menu_add_action_callback_factory.h"
#include "info/info_memento.h"
#include "core/application.h"
#include "main/main_domain.h"
#include <QtGui/QPainter>
#include <QShortcut>
#include <QKeySequence>
#include "lang/lang_keys.h"

namespace Window {

namespace {
	constexpr int kChatsId = 0;
	constexpr int kContactsId = 1;
	constexpr int kCallsId = 2;
	constexpr int kSavedId = 3;
	constexpr int kArchiveId = 4;
}

NavigationRail::NavigationRail(QWidget *parent, not_null<SessionController*> controller)
: Ui::RpWidget(parent)
, _controller(controller) {
	setupButtons();
	
	_controller->session().data().unreadBadgeChanges(
	) | rpl::start_with_next([this] {
		updateUnreadBadge();
	}, _lifetime);

	rpl::single(
		_controller->dialogsEntryStateCurrent()
	) | rpl::then(
		_controller->dialogsEntryStateValue()
	) | rpl::start_with_next([this](const Dialogs::EntryState &state) {
		if (state.key.folder() && state.key.folder()->id() == Data::Folder::kId) {
			setActiveNavId(kArchiveId);
		} else if (state.key.peer() == _controller->session().user()) {
			setActiveNavId(kSavedId);
		} else {
			setActiveNavId(kChatsId);
		}
	}, _lifetime);
}

NavigationRail::~NavigationRail() = default;

void NavigationRail::setupButtons() {
	auto createBtn = [&](int id, const style::icon &iconDef, const style::icon &iconAct) {
		auto btn = object_ptr<Ui::IconButton>(this, st::notifyClose); // Placeholder style, use default for now
		btn->setIconOverride(&iconDef, &iconAct);
		btn->setClickedCallback([=] { handleClick(id); });
		btn->show();
		_buttons.push_back({ std::move(btn), id });
	};

	createBtn(kChatsId, st::relayNavChats, st::relayNavChatsActive);
	createBtn(kContactsId, st::relayNavContacts, st::relayNavContactsActive);
	createBtn(kCallsId, st::relayNavCalls, st::relayNavCallsActive);
	createBtn(kSavedId, st::relayNavSaved, st::relayNavSavedActive);
	createBtn(kArchiveId, st::relayNavArchive, st::relayNavArchiveActive);

	_unreadBadge = object_ptr<Ui::UnreadBadge>(this);
	_unreadBadge->show();

	_settingsButton = object_ptr<Ui::IconButton>(this, st::notifyClose);
	_settingsButton->setIconOverride(&st::relayNavSettings, &st::relayNavSettingsActive);
	_settingsButton->setClickedCallback([this] { _controller->showSettings(); });
	_settingsButton->show();

	_profileButton = object_ptr<Ui::UserpicButton>(this, _controller->session().user(), st::defaultUserpicButton);
	_profileButton->setClickedCallback([this] { showProfileMenu(); });
	_profileButton->show();

	// Global Shortcuts for Relay Navigation
	auto scChats = new QShortcut(QKeySequence("Ctrl+1"), window());
	connect(scChats, &QShortcut::activated, [=] { handleClick(kChatsId); });
	
	auto scContacts = new QShortcut(QKeySequence("Ctrl+2"), window());
	connect(scContacts, &QShortcut::activated, [=] { handleClick(kContactsId); });
	
	auto scCalls = new QShortcut(QKeySequence("Ctrl+3"), window());
	connect(scCalls, &QShortcut::activated, [=] { handleClick(kCallsId); });

	auto scCommand = new QShortcut(QKeySequence("Ctrl+K"), window());
	connect(scCommand, &QShortcut::activated, [=] { _controller->showPeerHistory(_controller->session().userPeerId()); }); // Placeholder, or we can focus search.
}

void NavigationRail::updateUnreadBadge() {
	const auto count = _controller->session().data().unreadBadge();
	const auto muted = _controller->session().data().unreadBadgeMuted();
	if (count > 0) {
		_unreadBadge->setText(QString::number(count), !muted);
		_unreadBadge->show();
	} else {
		_unreadBadge->hide();
	}
	updateButtonsGeometry();
}

void NavigationRail::setActiveNavId(int id) {
	_activeNavId = id;
	update();
}

void NavigationRail::handleClick(int id) {
	setActiveNavId(id);
	switch (id) {
		case kChatsId:
			_controller->showBackFromStack();
			_controller->setActiveChatsFilter(0);
			break;
		case kContactsId:
			_controller->show(PrepareContactsBox(_controller));
			break;
		case kCallsId:
			::Calls::ShowCallsBox(_controller);
			break;
		case kSavedId:
			_controller->showPeerHistory(_controller->session().userPeerId());
			break;
		case kArchiveId:
			_controller->openFolder(_controller->session().data().folder(Data::Folder::kId));
			break;
	}
}

void NavigationRail::showProfileMenu() {
	if (_profileMenu) {
		_profileMenu = nullptr;
		return;
	}
	
	_profileMenu = base::make_unique_q<Ui::PopupMenu>(
		this,
		st::popupMenuExpandedSeparator);

	const auto controller = _controller;

	_profileMenu->addAction(tr::lng_menu_my_profile(tr::now), [=] {
		controller->showPeerInfo(controller->session().user());
	}, &st::menuIconProfile);

	_profileMenu->addAction(tr::lng_menu_settings(tr::now), [=] {
		controller->showSettings();
	}, &st::menuIconSettings);

	if (Core::App().domain().accounts().size() > 1) {
		_profileMenu->addSeparator();
		for (const auto &[index, account] : Core::App().domain().accounts()) {
			const auto isCurrent = (account == &controller->session().account());
			const auto name = account->sessionExists()
				? account->session().user()->name()
				: QString("Account %1").arg(index);
			_profileMenu->addAction(name, [=] {
				if (!isCurrent) {
					Core::App().domain().activate(account);
				}
			}, isCurrent ? &st::menuIconSavedMessages : nullptr); // check icon later
		}
	}
	
	_profileMenu->addSeparator();
	_profileMenu->addAction(tr::lng_mac_menu_add_account(tr::now), [=] {
		controller->showAddAccount();
	}, &st::menuIconAddMember);
	
	_profileMenu->popup(QCursor::pos());
}

void NavigationRail::updateAdaptiveLayout() {
	updateButtonsGeometry();
}

void NavigationRail::resizeEvent(QResizeEvent *e) {
	updateButtonsGeometry();
}

void NavigationRail::updateButtonsGeometry() {
	int y = 20;
	for (auto &b : _buttons) {
		b.button->moveToLeft((width() - b.button->width()) / 2, y);
		if (b.id == kChatsId && _unreadBadge && !_unreadBadge->isHidden()) {
			_unreadBadge->moveToLeft(b.button->x() + b.button->width() - _unreadBadge->width() / 2 - 5, b.button->y() - 5);
		}
		y += b.button->height() + 10;
	}
	
	if (_settingsButton && _profileButton) {
		int bottomY = height() - _profileButton->height() - 20;
		_profileButton->moveToLeft((width() - _profileButton->width()) / 2, bottomY);
		_settingsButton->moveToLeft((width() - _settingsButton->width()) / 2, bottomY - _settingsButton->height() - 10);
	}
}

void NavigationRail::paintEvent(QPaintEvent *e) {
	QPainter p(this);
	p.fillRect(e->rect(), st::windowBg);
	
	for (auto &b : _buttons) {
		if (b.id == _activeNavId) {
			auto rect = b.button->geometry();
			rect.adjust(-5, -5, 5, 5);
			p.setBrush(st::dialogsBgActive);
			p.setPen(Qt::NoPen);
			p.drawRoundedRect(rect, st::relayPanelRadius, st::relayPanelRadius);
		}
	}
}

} // namespace Window
