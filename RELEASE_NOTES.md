# Antigravity Timer v1.1.0 - macOS Stability Release

This release focuses on resolving critical stability issues and fixing UI/UX bugs in the macOS bundled application.

### Fixed
- **Fork Bomb Resolution**: Fixed a critical bug where the bundled `.app` would launch infinite instances of itself on startup.
- **Template Errors**: Resolved a `TemplateSyntaxError` caused by a missing `get_percent_color` filter.
- **Missing Routes**: Fixed a `NoReverseMatch` error by implementing the missing `bulk_update_account` view and URL pattern.
- **Repository Optimization**: Updated `.gitignore` to exclude large build/dist artifacts, keeping the repository lean.

### Features
- **Binary Distribution**: This release includes a pre-built macOS `.app` bundle for easy installation.

### Installation (macOS)
1. Download `AntigravityTimer_macOS.zip` from the assets below.
2. Unzip the file and move `AntigravityTimer.app` to your Applications folder.
3. Open the app to start tracking your accounts.
