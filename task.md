# Task: Phase C.6 — Build, Installer, Runtime Verification

Owner: (assign to a human operator)

Steps:

1. Trigger Windows CI (or run `build\build.bat` locally).
2. Collect build logs and confirm `Relay.exe` produced.
3. Retrieve installer artifact (`tsetup*.exe`) and run on a clean Windows VM.
4. Verify Start Menu/Desktop/uninstall entries display `Relay`/`Relay Desktop`.
5. Launch app and run runtime checklist (navigation, chats, settings, send/receive).
6. Update `RELAY_BUILD_STATUS.md` with results and paste logs.
7. If any compatibility regressions found (e.g., missing Updater, renamed internal files), stop and open an issue for migration planning.

Latest CI rerun result:

- Run: [31267417903](https://github.com/kelvinkbk/Relay/actions/runs/31267417903)
- Branch: `ci-rerun-716cefb4e0`
- Outcome: FAILED during CMake configure, not during dav1d fetch.
- Exact failure: missing `Relay/ThirdParty/MicroTeX/res/bundled.qrc` from `cmake/external/microtex/CMakeLists.txt`.
- Cache: miss.
- Submodule warning: `cmake` checkout warned about `not our ref a5bb7c5a86e3d0616984f7f6eaee359fdbd9bb5a`, but checkout completed.

Notes:

- Do NOT commit or push packaging fixes automatically; review results first.
- If installer or build fails, capture logs and attach to the task.
