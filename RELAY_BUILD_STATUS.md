# RELAY_BUILD_STATUS

This file records the CI/build/installer/runtime verification results for Phase C.6.

STATUS SUMMARY

- CI run: FAILED
- CI run ID: 31267417903
- CI branch: ci-rerun-716cefb4e0
- CI commit: e1f8595a6e
- Build result: FAILED (CMake configure failure)
- Installer result: NOT PRODUCED
- Runtime verification: NOT RUN

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

CI failure classification

- Root cause: CMAKE CONFIGURE FAILURE in `cmake/external/microtex/CMakeLists.txt`.
- Exact error: `Cannot find source file: D:/a/Relay/Relay/Relay/ThirdParty/MicroTeX/res/bundled.qrc`.
- This rerun did reach and complete dependency preparation, so the earlier dav1d timeout is not the blocking failure in this run.

Observed cache and checkout behavior

- Dependency cache: MISS for `relay-deps-win64-v1-c67a44aa42c1180007eb685c4c37e89938d7a85e97cc30f53c66acfd48c33f39`.
- Submodule warning: `fatal: remote error: upload-pack: not our ref a5bb7c5a86e3d0616984f7f6eaee359fdbd9bb5a` followed by `Fetched in submodule path 'cmake', but it did not contain a5bb7c5a86e3d0616984f7f6eaee359fdbd9bb5a. Direct fetching of that commit failed.`
- Impact: the warning did not stop checkout; the `Checkout Submodules` step completed successfully and the job advanced to dependency preparation, cache restore, and CMake configure.

Recommended immediate actions

1. Fix the missing MicroTeX `bundled.qrc` source in the checkout or workflow inputs before expecting CMake to configure successfully.
2. If you want to distinguish the older dav1d network issue from this CMake failure, rerun the same workflow again only after the checkout path is corrected.
3. If the rerun still fails, capture the new failing step and stop before making source changes.

CI rerun summary

- Workflow: `Build Relay Executable (Windows x64)`
- Run: [31267417903](https://github.com/kelvinkbk/Relay/actions/runs/31267417903)
- Branch: `ci-rerun-716cefb4e0`
- Outcome: dependency preparation completed, CMake generation failed, no Relay.exe artifact produced.

GitHub CLI command used:

```bash
gh workflow run build_relay.yml -R kelvinkbk/Relay --ref ci-rerun-716cefb4e0
```

SUBMODULE WARNING (observed in CI)

- Message: `Fetched in submodule path 'cmake', but it did not contain that commit: a5bb7c5a86e3d0616984f7f6eaee359fdbd9bb5a`
- Impact: The `Checkout Submodules` step logged the warning but dependency preparation continued. This warning did not cause the final failure in this rerun.

SUCCESS CONDITION

- Do not mark the build successful until the workflow reaches CMake configuration, C++ compilation, linking, and produces `Relay.exe` (and installer artifacts if present).

If you want, I can inspect the MicroTeX checkout next and determine why `bundled.qrc` is missing.

RUNTIME CHECKS (to perform on test VM)

- Install produced `tsetup*.exe` on a clean VM.
- Verify Start Menu and Desktop shortcut show `Relay`.
- Verify uninstall entry shows `Relay`.
- Launch app and perform UI smoke tests (navigation, chat open, settings, send/receive).

Notes: Do NOT modify AppId, AppUserModelID, Telegram.exe, Updater.exe, BinaryName, or tsetup\* artifacts during this phase.
