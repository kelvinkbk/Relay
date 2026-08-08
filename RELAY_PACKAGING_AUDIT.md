# RELAY_PACKAGING_AUDIT

This document records identified packaging/build-related artifacts for a separate packaging identity audit. Do NOT modify these files in Phase C.3 — they're recorded here for classification and future review.

Items discovered:

- `build/setup.iss` (installer script) — contains product display names and installer metadata such as `MyAppShortName`, `MyAppName`, `MyAppPublisher`, `MyAppExeName`. Classification: USER_VISIBLE_PACKAGING
- `build/build.sh` (packaging/build helper) — sets `BinaryName="Telegram"` and influences produced artifact names (archives, packages). Classification: BUILD_INTERNAL
- `build/docker/build.sh` — dockerized build wrapper; sets `BinaryName="Telegram"` and packaging steps. Classification: BUILD_INTERNAL
- `Relay/CMakeLists.txt` — build target names and `add_executable`/OUTPUT_NAME may reference `Telegram` in checks and logs. Classification: COMPATIBILITY
- `Relay/build/setup.iss` (legacy packaging at repo root) — installer macros such as `MyAppName` `MyAppShortName` and `MyAppExeName`. Classification: USER_VISIBLE_PACKAGING
- `Release` / packaged artifact names discovered in build scripts: `tsetup.*`, `tsetup-x64.*`, `tsetup.$AppVersionStrFull.dmg`, `tsetup.$MacArch.$AppVersionStrFull.dmg`. Classification: USER_VISIBLE_PACKAGING
- Executable names referenced: `Telegram`, `Updater`, `Packer` — Classification: COMPATIBILITY (may be used by external scripts or OS integrations)

Notes:

- `BUILD_INTERNAL` items affect internal packaging steps; changes may be necessary to rename produced artifacts but require a separate Packaging Identity Audit to preserve compatibility with existing updater/launcher expectations.
- `USER_VISIBLE_PACKAGING` items are visible to end users (installer name, product name) and should be updated in a coordinated packaging/branding step.
- `COMPATIBILITY` items may be required by third-party integrations and OS features and need careful migration planning.
- `UNKNOWN` not used here.

No changes made in this Phase. This file created to centralize packaging items for the Packaging Identity Audit.

## Phase C.4 — Packaging Identity Audit

| File                                                         | Symbol/Field                                                | Current                                                           | Proposed                                          | Classification                          | Action                                                                                                                                       |
| ------------------------------------------------------------ | ----------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Relay/build/setup.iss                                        | `MyAppShortName`                                            | "Telegram"                                                        | `Relay`                                           | USER_VISIBLE_PACKAGING                  | Propose change during packaging step (user-visible).                                                                                         |
| Relay/build/setup.iss                                        | `MyAppName`                                                 | "Telegram Desktop"                                                | `Relay`                                           | USER_VISIBLE_PACKAGING                  | Propose change during packaging step (installer display).                                                                                    |
| Relay/build/setup.iss                                        | `MyAppPublisher`                                            | "Telegram FZ-LLC"                                                 | KEEP (legal)                                      | LEGAL                                   | Keep; requires legal review before change.                                                                                                   |
| Relay/build/setup.iss                                        | `MyAppExeName`                                              | "Telegram.exe"                                                    | `Relay.exe` (proposed)                            | NEEDS_SEPARATE_MIGRATION                | Executable filename used by updater/launcher — coordinate migration.                                                                         |
| Relay/build/setup.iss                                        | `MyAppId` / `AppId`                                         | GUID {53F4975...}                                                 | KEEP (compat)                                     | COMPATIBILITY                           | AppId used for uninstall/registry/updates; do NOT change without migration plan.                                                             |
| Relay/build/setup.iss                                        | `UninstallDisplayName` / `DefaultGroupName`                 | "Telegram Desktop"                                                | `Relay`                                           | USER_VISIBLE_PACKAGING                  | Proposal: change for user-facing installer UI.                                                                                               |
| Relay/build/build.sh / Relay/build/build.bat                 | `BinaryName` / `SetupFile` / `PortableFile`                 | `Telegram`, `tsetup.*`, `tportable.*`                             | KEEP (unless migrated)                            | BUILD_INTERNAL / USER_VISIBLE_PACKAGING | `tsetup*` and `tportable*` filenames are user-facing artifacts and also referenced by update tooling — treat as COMPATIBILITY-sensitive.     |
| Relay/CMakeLists.txt                                         | target `Telegram` / `OUTPUT_NAME "Relay"`                   | target name: `Telegram`, output name: `Relay`                     | KEEP (current)                                    | BUILD_INTERNAL / COMPATIBILITY          | Internal target kept as `Telegram` while output is `Relay` — preserve until packaging validated.                                             |
| Relay/SourceFiles/core/version.h                             | `AppName` / `AppFile`                                       | `AppName = "Relay"`, `AppFile = "Telegram"`                       | `AppName = Relay`, `AppFile` needs migration plan | MIXED                                   | `AppName` already Relay; `AppFile` (internal name) impacts updater/paths — requires migration planning.                                      |
| Relay/Resources/winrc/Updater.rc                             | `CompanyName`, `FileDescription`, `ProductName`             | "Telegram FZ-LLC", "Telegram Desktop Updater", "Telegram Desktop" | KEEP (legal/compat)                               | COMPATIBILITY / LEGAL                   | Updater resources visible in file properties and signing metadata — keep for compatibility and legal/signing continuity.                     |
| Relay/SourceFiles/platform/win/windows_app_user_model_id.cpp | `AppUserModelIdBase`                                        | "Telegram.TelegramDesktop" (or Store variant)                     | NEEDS_SEPARATE_MIGRATION                          | COMPATIBILITY                           | Windows AppUserModelID affects pinned shortcuts, taskbar, notifications — changing will orphan pinned shortcuts; requires planned migration. |
| Relay/build/\* (mac)                                         | `tsetup*.dmg`, `tsetup_template.dmg`, bundle `Telegram.app` | `tsetup` prefixed artifacts                                       | KEEP (compat)                                     | USER_VISIBLE_PACKAGING / COMPATIBILITY  | macOS DMG names and `tsetup` artifacts are user-visible and used by update tooling — do NOT rename without coordination.                     |
| Relay/SourceFiles/_other/updater_\*.cpp / Updater executable | updater binary and resource names                           | `Updater`, `Updater.exe`                                          | KEEP                                              | COMPATIBILITY                           | Updater executable and its resource strings are tied to update flow — treat as COMPATIBILITY.                                                |

### SAFE TO CHANGE

- Installer UI product display names shown to users: `MyAppName`, `MyAppShortName`, `DefaultGroupName`, `UninstallDisplayName` in `Relay/build/setup.iss` — these are user-visible and can be updated to `Relay` during a packaging pass.
- Desktop/Start Menu shortcut displayed text (shown in `Relay/build/setup.iss` and created via installer icons) — safe to change to `Relay` as part of installer updates.

### KEEP FOR COMPATIBILITY

- `AppId` (GUID) in `Relay/build/setup.iss` and `Relay/SourceFiles/core/version.h` — used for Windows uninstall registry entries and update/install logic; changing will break upgrade/uninstall recognition.
- `BinaryName` internal build identifier (`Telegram`) and Updater executable name/path — referenced across build scripts (`Relay/build/build.sh`, `Relay/build/build.bat`, `Relay/build/docker/build.sh`) and launcher/updater sources; keep unless a coordinated migration is planned.
- `tsetup.*`, `tsetup-x64.*`, `tportable.*`, and other `t*` artifact names — these are used by update tooling and distribution; leave unchanged until updater validated.
- Updater resources and `ProductName`/`FileDescription` in `Relay/Resources/winrc/Updater.rc` — affect signing, file properties, and update checks; keep for compatibility and legal/signing continuity.

### NEEDS SEPARATE MIGRATION

- `MyAppExeName` / `Telegram.exe` -> `Relay.exe`: executable filename change requires updating installer scripts, launcher paths, updater command-line expectations, AppUserModelID handling, pinned shortcuts, and possibly server-side update metadata. Plan: (1) map all places expecting `Telegram.exe`; (2) update update/launcher code to accept `Relay.exe`; (3) coordinate deploy so both names are accepted during transition.
- `AppUserModelIdBase` / AppUserModelID (`Telegram.TelegramDesktop`): changing will orphan pinned taskbar/Start Menu shortcuts and may affect Windows notifications — requires migration utility to update pinned shortcuts and Start Menu entries.
- `tsetup*` artifact names: if the updater expects `tsetup` patterns, renaming requires updating server-side and client-side update paths.
- Any registry keys or file-association identifiers that include `Telegram` (uninstall keys, file associations) — must be migrated carefully with a plan to preserve user data and backward compatibility.

## Summary / Recommended Next Steps (audit-only)

1. Treat `Relay` as the user-visible product name for installer UI and shortcuts (`MyAppName`, `MyAppShortName`, `DefaultGroupName`, `UninstallDisplayName`). Update these during a packaging pass only.
2. Preserve `AppId`, `BinaryName` (internal `Telegram`), `tsetup*` artifact names, `Updater` binary/resource strings, and `AppUserModelID` until a migration plan is created.
3. For any change of executable filename or AppUserModelID, create a separate phased migration plan that: identifies all code and scripts that reference the old names, updates launcher/updater to accept both names during transition, and provides a migration utility to fix pinned shortcuts and Start Menu entries on existing user systems.
4. Run a full cross-check (search + test packaging) in a separate Packaging Identity PR that updates only packaging files and includes smoke tests for install/uninstall/update on each platform.

**Status:** PHASE C.4 — PACKAGING AUDIT COMPLETE. NO SOURCE CHANGES. CI NOT RUN.

## Phase C.5 — Safe Packaging Branding Applied

Files modified (safe-to-change scope):

- `Relay/build/setup.iss` — active installer script used by Windows packaging workflow (referenced by `Relay/build/build.bat` and `Relay/build/build.sh`).

Exact fields modified in `Relay/build/setup.iss`:

| Field                  | Old value                                                 | New value                     |
| ---------------------- | --------------------------------------------------------- | ----------------------------- |
| `MyAppShortName`       | "Telegram"                                                | "Relay"                       |
| `MyAppName`            | "Telegram Desktop"                                        | "Relay Desktop"               |
| `DefaultGroupName`     | `{#MyAppName}` ("Relay Desktop" after `MyAppName` change) | `{#MyAppShortName}` ("Relay") |
| `UninstallDisplayName` | `{#MyAppName}` ("Relay Desktop")                          | `{#MyAppShortName}` ("Relay") |

Fields intentionally preserved (no change):

- `AppId` / GUID — unchanged (compatibility/registry identifier).
- `MyAppExeName` — remains `Telegram.exe` (updater/launcher compatibility).
- `MyAppPublisher` — remains `Telegram FZ-LLC` (legal/licensing).
- `BinaryName` / internal `Telegram` and `Updater` / `Updater.exe` — unchanged.
- `tsetup*`, `tportable*` artifact names — unchanged.
- `AppUserModelID` (`Telegram.TelegramDesktop`) — unchanged.

Installer script selection rationale:

- The Windows packaging commands in `Relay/build/build.bat` and `Relay/build/build.sh` invoke Inno Setup using the `setup.iss` located in `Relay/build/` (invoked as `"%FullScriptPath%setup.iss"`), so `Relay/build/setup.iss` is the active installer script. No other active `setup.iss` files are referenced by the Windows build scripts found in the repository root; therefore only `Relay/build/setup.iss` was modified. If you want, I can run a workspace scan to confirm there are no other `setup.iss` files used by alternative packaging pipelines.

Verification performed:

- Confirmed `MyAppShortName` = Relay and `MyAppName` = Relay Desktop in `Relay/build/setup.iss`.
- Confirmed `DefaultGroupName` and `UninstallDisplayName` now reference `{#MyAppShortName}` (Relay).
- Confirmed `AppId`, `MyAppExeName`, `MyAppPublisher`, `Updater` and `tsetup*` references left unchanged.

**Status:** PHASE C.5 — SAFE PACKAGING BRANDING COMPLETE. SOURCE PATCH APPLIED. BUILD NOT RUN. CI NOT RUN.

## Phase C.6 — Build & Installer Verification (PENDING)

Summary:

- I did not trigger CI from this environment. The repository was not built in CI here. Per instructions, no runtime or CI actions were performed.
- The safe packaging edits in `Relay/build/setup.iss` are applied locally.
- Next step is to run the existing Windows GitHub Actions workflow or build locally to verify compilation, installer creation, and runtime behavior.

Required verification checklist (manual or CI):

- [ ] Trigger Windows CI workflow (GitHub Actions).
- [ ] Confirm compilation completes and `Relay.exe` is produced in `out/Release`.
- [ ] Confirm installer (`tsetup*.exe`) is produced and Inno Setup compile succeeds.
- [ ] Run installer on a Windows test VM and confirm Start Menu, Desktop shortcut, and uninstall entry show `Relay`/`Relay Desktop`.
- [ ] Confirm compatibility identifiers unchanged: `Telegram.exe`, `Updater.exe`, `tsetup*`, `AppId`, `AppUserModelID`, `BinaryName`.
- [ ] If CI or installer fails, record errors here and revert packaging edits if necessary.

Action items for CI run (do not run here):

1. Use GitHub Actions UI or `gh` CLI to trigger the Windows workflow (the repository contains an existing Windows build workflow).
2. Collect build logs and artifact names and paste them under `RELAY_BUILD_STATUS.md`.
3. Perform installer verification on a clean Windows VM and record runtime checks in `RELAY_BUILD_STATUS.md`.

Status: PHASE C.6 — BUILD & INSTALLER VERIFICATION PENDING (NO CI RUN HERE).
