# Packaging & Verification Walkthrough

This is a concise checklist and command set to run Phase C.6 locally or via CI.

1. Trigger Windows CI (recommended)

- Actions UI: Repository → Actions → select Windows build workflow → Run workflow.
- Or use `gh workflow run <workflow.yml>`.

2. Local build (Windows)

- Open appropriate Native Tools Command Prompt.
- Run:

```powershell
cd Relay
call build\build.bat
```

3. Locate artifacts

- `out\Release\Relay.exe` — output binary (verify exists)
- `out\Release\%SetupFile%` — produced installer (tsetup\*.exe)

4. Installer verification (Windows VM)

- Copy installer to test VM, run installer, verify Start Menu/Desktop/uninstall names.

5. Runtime smoke test

- Launch app, check window title, About dialog, navigation, chats, settings.

6. Record findings in `RELAY_BUILD_STATUS.md` and update `RELAY_PACKAGING_AUDIT.md` as needed.
