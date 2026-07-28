# Relay Action Migration Matrix

This document tracks the migration of legacy Telegram Desktop hamburger menu actions to their new Relay-native locations.

| Old Location | Action | Existing Controller/Function | New Relay Location | Status |
|---|---|---|---|---|
| Main Menu | **User Profile / Avatar** | `controller->showSection(Info::Stories::Make(controller->session().user()))` | Navigation Rail (Bottom Avatar) | Pending |
| Main Menu | **Toggle Accounts** | `toggleAccounts()` / Settings | Navigation Rail (Bottom Avatar Menu) | Pending |
| Main Menu | **Add Account** | `Settings::SetupAccounts` (inner) | Navigation Rail (Bottom Avatar Menu) | Pending |
| Main Menu | **Set Emoji Status** | `chooseEmojiStatus()` | Navigation Rail (Bottom Avatar Menu) | Pending |
| Main Menu | **Archive** | `showArchive()` | Navigation Rail (`Archive` button) | Pending |
| Main Menu | **New Group** | `controller->showNewGroup()` | Dialogs Panel Header `[+]` Button & Command Menu | Pending |
| Main Menu | **New Channel** | `controller->showNewChannel()` | Dialogs Panel Header `[+]` Button & Command Menu | Pending |
| Main Menu | **Contacts** | `controller->show(PrepareContactsBox(controller))` | Navigation Rail (`Contacts` button) | Pending |
| Main Menu | **Calls** | `::Calls::ShowCallsBox(controller)` | Navigation Rail (`Calls` button) | Pending |
| Main Menu | **Saved Messages** | `controller->showPeerHistory(controller->session().user())` | Navigation Rail (`Saved` button) | Pending |
| Main Menu | **Settings** | `controller->showSettings()` | Navigation Rail (`Settings` button) & Command Menu | Pending |
| Main Menu | **Night Mode** | `Window::Theme::ToggleNightMode()` | Settings > Appearance | Pending |
| Main Menu | **About** | `(various about boxes)` | Settings > About Relay | Pending |
| Main Menu | **Search** | `(Global Search in Dialogs)` | Conversation Panel Header (Search input) | Pending |

## Hamburger Removal Blocker Checklist

Before the hamburger button is hidden, the following MUST be fully accessible via Relay-native UX:

- [ ] Account switching and Profile management (Avatar in Rail)
- [ ] Group/Channel creation (Header `[+]` button)
- [ ] Contacts and Calls (Rail)
- [ ] Saved Messages and Archive (Rail)
- [ ] Settings (Rail)
- [ ] Night Mode toggle (Settings > Appearance)
- [ ] About screen (Settings > About)
