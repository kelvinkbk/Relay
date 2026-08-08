# Phase 5.5 — Relay UI polish: Initial audit and plan

## Summary

- Repository-wide occurrences of user-visible "Telegram" branding found: ~940 matches across ~71 files (code, resources, docs, build files).
- Goal: remove remaining Telegram branding from user-visible UI while preserving protocol/networking/auth/storage and legal attribution where required.

## Top-priority visible items (first-pass)

1. Application identity
   - `Relay/CMakeLists.txt` (target name and output name currently reference "Telegram")
   - `Relay/Resources/winrc/Telegram.rc` (CompanyName, version resource)
   - `lib/xdg/org.telegram.desktop.desktop` and `lib/xdg/org.telegram.desktop.metainfo.xml`
   - `Relay/Resources/qrc/telegram/telegram.qrc` (resource paths)
   - `Relay/Resources/uwp/AppX/AppxManifest.xml` (Identity name)

2. Localized UI strings
   - `Relay/Resources/langs/lang.strings` and per-locale `Localizable.strings` files contain many user-visible strings referencing Telegram (FAQ, Premium, Update text, About text, etc.).

3. About / window title / splash / tray
   - About dialog strings live in localized resources and in code that composes the About text.
   - Window title may be set from build-time metadata or strings in code.
   - Tray icon names and art referenced in `branding/` and `lib/xdg` files.

4. Legal & docs
   - `LEGAL`, `CMakeLists.txt` headers, README and many docs still reference Telegram Desktop. Keep legal attribution intact; update docs to reference Relay where appropriate but do not remove required TELEGRAM legal lines.

5. UI elements left as Telegram remnants
   - Profile popup, navigation rail, dialogs list, settings labels (e.g., "About Telegram"), tooltips and menu labels.
   - Stylesheets and icons may still use Telegram-specific names or classes.

## Action plan (iterative, compile-after-each-change)

Per your constraints: no protocol/auth/networking/storage changes; stop large architectural changes. Work will be small, incremental edits with build+run verification.

Phase A — Audit & safe replacements (this PR)

- Create a canonical inventory of user-visible occurrences (this document).
- For each candidate: classify as (A) safe UI text replacement, (B) legal/attribution (do not remove), or (C) code/ID/manifest (update carefully).

Phase B — Identity fixes (low-risk, high-impact)

- Update `lib/xdg/org.telegram.desktop.desktop` metadata to Relay equivalents.
- Update `Relay/Resources/winrc/Telegram.rc` CompanyName and product strings to Relay.
- Update `Relay/Resources/uwp/AppX/AppxManifest.xml` Identity to Relay name.
- Update `Relay/CMakeLists.txt` comments/headers where safe (leave LICENSE/LEGAL references intact), ensure output name remains `Relay` (already set).
- Build & run

Phase C — Localized strings (UI text)

- For each `lang.strings` entry that is user-visible and not legal/protocol-related, perform a text replacement: "Telegram" -> "Relay" and "Telegram Desktop" -> "Relay by TheonixOS" as appropriate.
- Keep context-sensitive strings (e.g., links pointing to telegram.org) flagged for manual review.
- Build & run

Phase D — About dialog, tray, splash, icons

- Replace About title and content with Relay branding (preserve legal section verbatim where required).
- Replace tray icon metadata to `relay` naming; confirm `branding/` has correct art assets.
- Build & run

Phase E — UI polish work (visual changes)

- Profile popup redesign: small, iterative visual edits (spacing, typography, icons). Update relevant UI files and styles in `Relay/SourceFiles` and `Relay/lib_ui`.
- Navigation rail polish: spacing/alignment/active indicator/hover animations. Change style variables and icons; compile-run-verify.
- Dialogs panel and Chat view adjustments: spacing, padding, empty states.
- Settings: rename visible labels (About Relay, Appearance, Dark Mode).
- Each subtask will be committed and verified separately.

Phase F — Documentation

- Update `walkthrough.md`, `task.md`, `implementation_plan.md`, and `RELAY_BUILD_STATUS.md` with what changed and verification notes.

## Notes and constraints

- Legal files that explicitly state "This file is part of Telegram Desktop" should remain for attribution; if the license mandates text, preserve it.
- Do NOT modify MTProto, auth, networking, or storage code. Avoid touching code paths that affect protocol behavior.
- Every logical group of edits will be followed by build + run verification.

## Next step (proposed)

1. Confirm you want me to proceed with Phase B identity fixes now (I will change desktop metadata, win resource strings, and UWP Identity). I will build after those edits and report results.
2. If confirmed, I'll perform small, targeted edits and run the build. If you prefer, I can first present a proposed diff for review before applying.

End of initial audit.
