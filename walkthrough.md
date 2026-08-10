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

Latest CI rerun result:

- Workflow run: [31267417903](https://github.com/kelvinkbk/Relay/actions/runs/31267417903)
- Branch: `ci-rerun-716cefb4e0`
- Outcome: dependency preparation completed, but CMake generation failed in `cmake/external/microtex/CMakeLists.txt` because `Relay/ThirdParty/MicroTeX/res/bundled.qrc` was missing.
- Dependency cache status: miss.
- Submodule warning: `cmake` submodule checkout reported `not our ref a5bb7c5a86e3d0616984f7f6eaee359fdbd9bb5a`, but checkout continued.
