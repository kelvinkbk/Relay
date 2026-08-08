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

Notes:

- Do NOT commit or push packaging fixes automatically; review results first.
- If installer or build fails, capture logs and attach to the task.
