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

## Phase 6 — Relay Runtime Polish Status

- BUILD: PENDING — latest CI blocked at CMake configuration
- EXECUTABLE: NOT VERIFIED FOR CURRENT PHASE 6 SOURCE
- RUNTIME: PREVIOUS BUILD VERIFIED, CURRENT SOURCE NOT YET VERIFIED

Summary of Phase 6 local source polish applied:
1. **Login UI**: Replaced "Scan From Mobile Relay" / "Open Relay on your phone" with "Scan from your phone" / "Open your mobile app". Updated QR accent color to Relay Primary Indigo (`#6366F1`).
2. **Chat Wallpaper**: Removed Telegram doodle pattern (`background.tgv`) loading in `window_theme.cpp` and `window_theme_preview.cpp`. Configured neutral surface gradient (`#F5F6F8`, `#EBEDF0`) in `data_wall_paper.cpp`.
3. **Relay Colors**: Updated `msgOutBg` to `#EEF0FF` in `colors.palette` and updated embedded scheme accent color to `#6366F1` in `window_themes_embedded.cpp`.
4. **Navigation Rail & Profile**: Expanded profile menu in `window_navigation_rail.cpp` to expose Profile, Edit Profile, Settings, Account switching, Add Account, and Sign out.
5. **Settings**: Removed duplicate Night Mode entry in `settings_main.cpp` outside of `Settings > Appearance`.
