#pragma once

#include "ui/rp_widget.h"
#include "base/object_ptr.h"
#include "ui/controls/userpic_button.h"
#include "ui/unread_badge.h"

namespace Ui {
class IconButton;
class PopupMenu;
} // namespace Ui

namespace Window {

class SessionController;

class NavigationRail final : public Ui::RpWidget {
public:
	NavigationRail(QWidget *parent, not_null<SessionController*> controller);
	~NavigationRail();

	void updateAdaptiveLayout();

protected:
	void paintEvent(QPaintEvent *e) override;
	void resizeEvent(QResizeEvent *e) override;

private:
	void setupButtons();
	void updateButtonsGeometry();
	void handleClick(int index);
	void updateUnreadBadge();
	void setActiveNavId(int id);
	void showProfileMenu();

	const not_null<SessionController*> _controller;
	rpl::lifetime _lifetime;

	struct NavButton {
		object_ptr<Ui::IconButton> button;
		int id;
	};

	std::vector<NavButton> _buttons;
	object_ptr<Ui::IconButton> _settingsButton = { nullptr };
	object_ptr<Ui::UserpicButton> _profileButton = { nullptr };
	object_ptr<Ui::UnreadBadge> _unreadBadge = { nullptr };
	base::unique_qptr<Ui::PopupMenu> _profileMenu;
	
	int _activeNavId = 0;
};

} // namespace Window
