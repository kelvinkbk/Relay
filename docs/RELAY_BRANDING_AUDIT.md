# RELAY_BRANDING_AUDIT — Phase C

## Purpose

This document records a workspace-wide audit of remaining "Telegram" branding in the Relay codebase and classifies occurrences for safe action during Phase C.

## Summary of automated scan

- Matches for canonical tokens across the workspace (initial quick scan):
  - "Telegram" / case-insensitive: ~940 occurrences across ~71 files (workspace-wide)
  - In `Relay/` tree: 800 occurrences across 82 files (includes build scripts, resources, docs, localized strings)

## Methodology

- Searched for the tokens: `Telegram`, `telegram`, `TELEGRAM`, `Telegram Desktop`, `TelegramDesktop`, `t.me`, `tg://` within the repository.
- Each hit was classified into one of these categories:
  A. USER_VISIBLE_BRANDING — visible UI/product strings or metadata that should be replaced with Relay branding.
  B. TELEGRAM_SERVICE — references to Telegram service, API, MTProto, payment/features; keep unchanged.
  C. LEGAL_ATTRIBUTION — license, copyright, or required legal text; keep unchanged.
  D. COMPATIBILITY_IDENTIFIER — protocol names, DB keys, deep-link handlers, binary/IPC identifiers; keep unless proven safe to change.
  E. LEGACY_PRODUCT_UI — legacy UI identifiers that are user-visible and safe to replace.

## High-priority USER_VISIBLE_BRANDING (recommend immediate safe replacements)

- `Relay/Resources/winrc/Telegram.rc` — FileDescription/ProductName shown in Windows File Properties. (A) — already updated `ProductName`/`CompanyName` in Phase B.
- `lib/xdg/org.telegram.desktop.desktop` — Desktop entry `Name`, `Comment`, `Exec`, `Icon` are user-visible (A) — already updated in Phase B; verify `StartupWMClass` at runtime.
- `lib/xdg/org.telegram.desktop.metainfo.xml` — AppStream metadata `name`, `summary`, `screenshots` description text (A) — partially updated in Phase B; remaining links point to Telegram — see URL policy below.
- `Relay/Resources/uwp/AppX/AppxManifest.xml` — DisplayName / Description (A) — updated in Phase B.
- `Relay/Resources/qrc/telegram/telegram.qrc` — resource alias paths to UI assets and icons; some aliases are user-visible (A) — qrc alias updated in Phase B; consider renaming other icon aliases (e.g., `plane_white.svg`) only if asset contains Telegram-exclusive imagery.
- `branding/RELAY_BRAND_GUIDE.md` — update instructions reference Telegram; user-visible branding guidance (A).

## High-priority KEEP (do not change without verification)

- `Relay/Resources/langs/lang.strings` and per-locale `Localizable.strings` — Contains many user-visible strings referencing Telegram features (Premium, Passport, FAQ links). Classification: mix of A and B — requires per-string manual review (see Language Files section below). _Do not apply blind global replacement._
- `Relay/CMakeLists.txt` and many `cmake/*` files — build targets, function names, script comments reference Telegram. Classification: D (compatibility/identifier). Leave until runtime/CI proves safe to change.
- `LEGAL`, license headers and copyright notices — C (legal attribution) — keep.
- `Relay/ThirdParty/*` and submodules — B/C depending on whether they reference Telegram as upstream projects; keep.

## URLs and external links

- Many metadata files still reference telegram.org, GitHub repos for Telegram, and other Telegram service URLs. Policy: do NOT invent new Relay URLs. For now, mark as PENDING — VERIFIED URL REQUIRED when a canonical Relay site exists.

## Language files (detailed guidance)

- `Relay/Resources/langs/lang.strings` contains many entries that mention Telegram in feature names and help text (e.g., Premium, Passport, updates). These fall into two subcategories:
  - Service/feature references (B) — keep (e.g., "Telegram Premium", API/Passport references).
  - Product UI references (A) — safe to rename (e.g., "Telegram Desktop" -> "Relay Desktop", "About Telegram" -> "About Relay").
- Plan: produce a filtered list of candidate language keys that contain the exact substring "Telegram Desktop" or "About Telegram" and propose replacements one-by-one for review.

## Icons and art

- Search results include many graphical assets (icons/plane, tray icons, logos). Action:
  - If an asset contains Telegram-specific imagery (paper plane, distinct Telegram blue) and is visible in the app chrome, replace with Relay art from `branding/` where available.
  - If an asset is generic (e.g., paper plane used for send button but not trademarked in context of the Telegram service) consider keeping if replacement causes no UI regression; flag for manual review.

## Desktop / OS integration

- Protocol handlers (`tg://`, `t.me`) are compatibility identifiers; DO NOT remove. If we want Relay-specific handlers, plan externally. Class: D — keep.
- AppUserModelID / executable names: `add_executable(Telegram ...)` in `Relay/CMakeLists.txt` — D; currently OUTPUT_NAME set to "Relay"; keep source-level target name unchanged until CI/runtime verified.

## Quick counts (approx.)

- Total initial matches (workspace): ~940
- Matches in `Relay/` tree: ~800
- Files containing hits: ~80

## Planned Phase C safe steps (iterative)

1. Produce a candidate diff for the following non-language files (safe):
   - `lib/xdg/org.telegram.desktop.desktop` (already updated)
   - `lib/xdg/org.telegram.desktop.metainfo.xml` (already updated)
   - `Relay/Resources/winrc/Telegram.rc` (already updated)
   - `Relay/Resources/uwp/AppX/AppxManifest.xml` (already updated)
   - `Relay/Resources/qrc/telegram/telegram.qrc` (aliases updated)
   - Build/install scripts that only mention product display names (e.g., installer comments) — propose selective changes.

2. Prepare a curated list of language keys from `Relay/Resources/langs/lang.strings` that contain exact UI product strings such as "Telegram Desktop", "About Telegram", and present them for review.

3. Search and list any icons that are clearly Telegram-branded (paper plane, telegram blue) and propose replacements from `branding/` where available.

4. For each logical set of replacements: generate a branch, commit, and trigger CI build. Do not batch unrelated edits.

## Next actions I will take (unless you instruct otherwise)

1. Generate a curated list of language string keys that contain the exact substring "Telegram Desktop", "About Telegram", or start with "lng\_...telegram..." for manual review. I will add this list to this audit document as a sub-section.
2. Prepare a small candidate diff for only the non-language, clearly user-visible metadata files that are safe to change (I have already applied Phase B changes). I will show the diff before committing (unless you tell me to commit directly).

Please confirm whether you want me to:

- (A) Proceed to auto-generate the curated language-key list now and present it for review, then apply only reviewed entries; or
- (B) Apply a safe metadata-only commit now and open a branch/PR for CI; or
- (C) Pause and let you run CI first to validate Phase B changes.

Audit file generated by: Copilot assistant (local workspace scan)
Location: `docs/RELAY_BRANDING_AUDIT.md`

## Phase C.1 — Curated Language Candidates

Summary:

- Candidates found that match the requested product-identity phrases ("Telegram Desktop", "About Telegram", "Telegram Desktop version", "Telegram application", "Telegram client").
- Total candidate files matching these phrases in language files: 9 header/comment files + multiple language keys in `lang.strings` that reference "About Telegram Premium" and related service strings.

Detailed candidates:

1. FILE: `Relay/Resources/langs/cloud_lang.strings`
   LANGUAGE: (cloud)
   KEY: HEADER_COMMENT
   CURRENT VALUE: "This file is part of Telegram Desktop, the official desktop application for the Telegram messaging service."
   PROPOSED VALUE: KEEP (legal attribution)
   CLASSIFICATION: LEGAL_ATTRIBUTION
   REASON: File header legal attribution; must be preserved verbatim per repository license and upstream attribution.

2. FILE: `Relay/Resources/langs/en.lproj/Localizable.strings`
   LANGUAGE: English (en.lproj)
   KEY: HEADER_COMMENT
   CURRENT VALUE: "This file is part of Telegram Desktop, the official desktop application for the Telegram messaging service."
   PROPOSED VALUE: KEEP
   CLASSIFICATION: LEGAL_ATTRIBUTION
   REASON: File header legal attribution; do not change.

3. FILE: `Relay/Resources/langs/de.lproj/Localizable.strings`
   LANGUAGE: German (de.lproj)
   KEY: HEADER_COMMENT
   CURRENT VALUE: "This file is part of Telegram Desktop, the official desktop application for the Telegram messaging service."
   PROPOSED VALUE: KEEP
   CLASSIFICATION: LEGAL_ATTRIBUTION
   REASON: File header legal attribution; do not change.

4. FILE: `Relay/Resources/langs/es.lproj/Localizable.strings`
   LANGUAGE: Spanish (es.lproj)
   KEY: HEADER_COMMENT
   CURRENT VALUE: "This file is part of Telegram Desktop, the official desktop application for the Telegram messaging service."
   PROPOSED VALUE: KEEP
   CLASSIFICATION: LEGAL_ATTRIBUTION
   REASON: File header legal attribution; do not change.

5. FILE: `Relay/Resources/langs/it.lproj/Localizable.strings`
   LANGUAGE: Italian (it.lproj)
   KEY: HEADER_COMMENT
   CURRENT VALUE: "This file is part of Telegram Desktop, the official desktop application for the Telegram messaging service."
   PROPOSED VALUE: KEEP
   CLASSIFICATION: LEGAL_ATTRIBUTION
   REASON: File header legal attribution; do not change.

6. FILE: `Relay/Resources/langs/ko.lproj/Localizable.strings`
   LANGUAGE: Korean (ko.lproj)
   KEY: HEADER_COMMENT
   CURRENT VALUE: "This file is part of Telegram Desktop, the official desktop application for the Telegram messaging service."
   PROPOSED VALUE: KEEP
   CLASSIFICATION: LEGAL_ATTRIBUTION
   REASON: File header legal attribution; do not change.

7. FILE: `Relay/Resources/langs/nl.lproj/Localizable.strings`
   LANGUAGE: Dutch (nl.lproj)
   KEY: HEADER_COMMENT
   CURRENT VALUE: "This file is part of Telegram Desktop, the official desktop application for the Telegram messaging service."
   PROPOSED VALUE: KEEP
   CLASSIFICATION: LEGAL_ATTRIBUTION
   REASON: File header legal attribution; do not change.

8. FILE: `Relay/Resources/langs/pt-BR.lproj/Localizable.strings`
   LANGUAGE: Portuguese (pt-BR.lproj)
   KEY: HEADER_COMMENT
   CURRENT VALUE: "This file is part of Telegram Desktop, the official desktop application for the Telegram messaging service."
   PROPOSED VALUE: KEEP
   CLASSIFICATION: LEGAL_ATTRIBUTION
   REASON: File header legal attribution; do not change.

9. FILE: `Relay/Resources/langs/lang.strings`
   LANGUAGE: English (main `lang.strings`)
   KEY: `lng_sessions_about_apps`
   CURRENT VALUE: "The official Telegram app is available for Android, iPhone, iPad, Windows, macOS and Linux."
   PROPOSED VALUE: KEEP
   CLASSIFICATION: TELEGRAM_SERVICE
   REASON: This string references the Telegram mobile/other clients (service ecosystem) rather than the Relay product; keep as-is.

10. FILE: `Relay/Resources/langs/lang.strings`
    LANGUAGE: English
    KEY: `lng_profile_unofficial_warning`
    CURRENT VALUE: "{icon} {name} uses an unofficial Telegram client — messages to this user may be less secure."
    PROPOSED VALUE: KEEP
    CLASSIFICATION: TELEGRAM_SERVICE
    REASON: Refers to third-party/ unofficial Telegram clients — service-level security warning; do not change.

11. FILE: `Relay/Resources/langs/lang.strings`
    LANGUAGE: English
    KEY: `lng_premium_more_about`, `lng_premium_summary_bottom_subtitle`, `lng_premium_gift_terms` (representative keys)
    CURRENT VALUES: "About Telegram Premium", "About Telegram Premium", "You can review the list of features and more details about Telegram Premium {link}."
    PROPOSED VALUE: KEEP
    CLASSIFICATION: TELEGRAM_SERVICE
    REASON: These are service/feature references (Telegram Premium) and must remain unchanged.

Notes:

- I limited candidates to occurrences that contain one of the requested product phrases. Most matches in `lang.strings` refer to Telegram service features (Premium, Stars, Passport, API) and are classified as TELEGRAM_SERVICE (KEEP).
- Several header comments in localized `Localizable.strings` files contain the phrase "This file is part of Telegram Desktop" — these are legal attributions (KEEP).
- No UI keys in `lang.strings` were found that directly use the product-string "Telegram Desktop" as a visible label (for example "About Telegram" used as a top-level About label). Many UI labels already read "About" or "Open Relay" and appear to have been adapted earlier.

## COUNT SUMMARY

- Header files with "This file is part of Telegram Desktop": 9 (kept as LEGAL_ATTRIBUTION)
- `lang.strings` keys referencing "Telegram client/app/service": dozens (classified as TELEGRAM_SERVICE and kept)
- Direct UI product-name candidates (to replace): 0 found in `lang.strings` matching the requested product-identity phrases after filter and manual review.

## Next steps (proposed)

1. If you want, I can generate a safe, curated list of language keys that are explicitly UI product labels (for example if any string equals "Telegram Desktop" or "About Telegram") — but the initial scan shows none in `lang.strings` requiring replacement.
2. If you prefer me to search more broadly (outside `Relay/Resources/langs`) for UI-label occurrences, I can do that and present candidates.

## PHASE C.1 STATUS

AUDIT COMPLETE
CHANGES NOT APPLIED
CI NOT RUN

## Phase C.3 — Applied Safe Runtime Branding

The following safe runtime branding changes were applied in Phase C.3 (audit-only, no commits pushed):

- `Relay/SourceFiles/boxes/about_box.cpp` — Replaced the private-alpha clipboard informational message to reference "Relay" instead of "Telegram Desktop" so the About dialog message matches product identity.
- `Relay/SourceFiles/core/crash_report_window.cpp` — Replaced hardcoded fallback window title `u"Telegram"_q` with `AppName.utf16()` so pre-launch/crash window follows the application identity.
- `Relay/SourceFiles/platform/mac/window_title_mac.mm` — Replaced hardcoded preview title `u"Telegram"_q` with `AppName.utf16()` and included `core/version.h` to source the application name.
- `Relay/SourceFiles/platform/mac/global_menu_mac.mm` — Replaced the hardcoded "Show Telegram" action with `tr::lng_mac_menu_show(tr::now)` and switched the top-level Apple menu display name to `AppName.utf16()`. Updated the About menu to use `tr::lng_mac_menu_about_telegram(tr::now, lt_telegram, AppName.utf16())` so About/Quit translations receive the current app name.
- `Relay/SourceFiles/platform/linux/main_window_linux.cpp` — Replaced literal `u"Telegram"_q` arguments used to construct user-visible Quit/About menu labels with `AppName.utf16()` so the Linux global menu labels follow application identity while preserving localization keys.

Verification steps performed:

1. Targeted diffs and replacements limited to the files above.
2. Searched modified files to confirm only the intended string substitutions were applied.
3. Created `RELAY_PACKAGING_AUDIT.md` to record packaging/build artifacts for a future packaging audit (no build scripts modified in this phase).

Status: SAFE PATCH COMPLETE — the runtime branding edits above have been applied locally. See `RELAY_PACKAGING_AUDIT.md` for packaging items recorded.
