# Relay UI Architecture

This document outlines the UI component tree and existing application controllers in the Relay (formerly Telegram Desktop) codebase, specifically evaluating their readiness for the three-column Relay Navigation layout.

## 1. Existing Component Tree & Layout

- **Main Application Window (`MainWindow` / `Window::Controller`)**
  - Manages the overall window frame, OS-level window events, and holds the `SessionController`.
- **`SessionController` (`window_session_controller.h`)**
  - Manages navigation, state, and coordinates active views (Dialogs, Chat, Info panels) for a single user session.
- **`MainWidget` (`mainwidget.h`)**
  - The central layout widget. It currently implements a responsive adaptive layout that shifts between one, two (`Normal`), and three columns (`ThreeColumn`).
  - Contains `_dialogs` (Conversation list column).
  - Contains `_history` (Active conversation column).
  - Contains `_thirdSection` (Info panel / Tabbed selector).
- **Navigation Menu (`Window::MainMenu`)**
  - Currently implemented as a `Ui::LayerWidget` (a sliding popup drawer) that contains settings, accounts, archive, and contacts.

## 2. Adaptive Layout (`Window::Adaptive::WindowLayout`)
The existing layout system defined in `window_adaptive.h` relies on three enum states:
- `OneColumn`: Dialogs list OR History view fills the screen.
- `Normal`: Two columns (Dialogs list + History view).
- `ThreeColumn`: Three columns (Dialogs + History + Info/Tabbed Selector).

## 3. Plan for Relay Navigation Rail
To achieve the requested target layout (`[ NAV ] [ CONVERSATIONS ] [ ACTIVE CONVERSATION ]`):

1. **Insert a Permanent Left Navigation Rail**
   - Create a new `RelayNavigationRail` widget.
   - Inject it into `MainWidget` as the leftmost fixed-width column.
2. **Shift Existing Columns**
   - The current `_dialogs` widget will act as the middle column (Conversations).
   - The current `_history` widget will act as the right column (Active Conversation).
3. **Connect Existing Controllers**
   - **Chats**: `_controller->showBackFromStack()` or activate `_dialogs`.
   - **Contacts**: `_controller->show(Box<ContactsBox>(...))`.
   - **Calls**: `_controller->show(Box<CallsBox>(...))`.
   - **Saved Messages**: `_controller->showPeerHistory(session().user()->id)`.
   - **Archive**: `_controller->showFolder(Data::Folder::kArchiveId)`.
   - **Settings**: `_controller->showSettings()`.

## 4. MoveOldDataFiles Review
**Original Upstream Implementation (`logs.cpp`)**
- **Files Migrated**: `data`, `data_config`, `tdata/config`.
- **Source Paths**: `wasDir` (derived from `psAppDataPathOld()`, pointing to `%APPDATA%\Telegram Desktop\`).
- **Destination Paths**: `cWorkingDir()` (pointing to `%APPDATA%\Relay\`).
- **Execution**: Ran during `Logs::start()`.
- **Decision**: The upstream logic explicitly existed to migrate from legacy standalone Telegram paths into `%APPDATA%\Telegram Desktop\`. Because Relay uses `%APPDATA%\Relay\` securely, and `wasDir` would point to Telegram Desktop data, allowing this function to run would cause Relay to mistakenly consume the user's Telegram Desktop session. Deleting it is the correct architectural decision. Relay-to-Relay updates will inherently reuse `%APPDATA%\Relay\` without needing migration.
