# RELAY_BUILD_STATUS

This file records the CI/build/installer/runtime verification results for Phase C.6.

STATUS SUMMARY

- CI run: NOT RUN (manual trigger required)
- Build result: FAILED (local attempt)
- Installer result: PENDING
- Runtime verification: PENDING

ARTIFACTS (expected)

- Executable: Relay.exe (output name)
- Internal executable: Telegram.exe (preserved)
- Updater: Updater.exe (preserved)
- Installer: tsetup\*.exe (preserved naming)

HOW TO TRIGGER THE WINDOWS CI (manual)

- In GitHub Actions UI: open the repository → Actions → select the Windows build workflow → Run workflow (choose branch).
- Using GitHub CLI (if authenticated):

```bash
gh workflow run "windows.yml" --ref main
```

LOCAL BUILD (Windows quick commands)

1. Open "x64 Native Tools Command Prompt for VS 2022" (or appropriate arch).
2. From repository root (`Relay`):

```powershell
cd Relay
call build\build.bat
```

Record CI/build logs and paste them below after running.

LOCAL BUILD ATTEMPT (executed by assistant)

- Command run (from repository root):

```powershell
cd Relay
call build\build.bat
```

- Observed output (exact):

```
This script is for building the production version of Telegram Desktop.

For building custom versions please visit the build instructions page at:
https://github.com/telegramdesktop/tdesktop/#build-instructions
```

- Exit reason: `build.bat` aborted early because required `DesktopPrivate` directory is missing from the workspace (build scripts check for `DesktopPrivate` and exit if absent). This environment does not contain the private packaging/signing assets required by the production build script.

GIT COMMIT

- Current commit SHA: e1f8595a6e

NEXT STEPS / REMEDIATION

1. Run CI on GitHub Actions (recommended). The repository's CI environment typically provides the required `DesktopPrivate` secrets and signing helpers that are not present locally.
2. Or provide a `DesktopPrivate` folder with the expected structure and any required signing artifacts on the build machine (not recommended for public systems).
3. If you want me to run additional local troubleshooting, I can rerun the build after you provide the missing artifacts or instruct me to invoke the CI via the GitHub workflow (requires permission).

RUNTIME CHECKS (to perform on test VM)

- Install produced `tsetup*.exe` on a clean VM.
- Verify Start Menu and Desktop shortcut show `Relay`.
- Verify uninstall entry shows `Relay`.
- Launch app and perform UI smoke tests (navigation, chat open, settings, send/receive).

Notes: Do NOT modify AppId, AppUserModelID, Telegram.exe, Updater.exe, BinaryName, or tsetup\* artifacts during this phase.
