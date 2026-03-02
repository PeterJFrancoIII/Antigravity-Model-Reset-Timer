# Contributing to Antigravity Model Reset Timer

First off, thank you for considering contributing to the Antigravity Model Reset Timer! It's people like you that make this tool great. We are actively looking for developers, designers, and prompt engineers to help evolve this project from a standalone desktop app into a native extension of the autonomous Antigravity AI ecosystem.

## How Can I Contribute?

### 1. Develop Future Integration Features
Our immediate roadmap (`project_descriptor.md`) outlines three major phases of development. We need help building:
- **Phase 1: Automated Telemetry**: Securely hooking into the Google AI Studio and Anthropic Console APIs to automatically poll rate limits without manual entry.
- **Phase 2: Local IPC**: Building a lightweight local REST/WebSocket server so the main Antigravity agent can query its own usage quotas before starting heavy workflows.
- **Phase 3: Native IDE/CLI Integrations**: Porting the existing webview dashboard into a Visual Studio Code extension or a native plugin for the Antigravity CLI.

### 2. Improve the Current Codebase
- **Frontend**: The dashboard uses Vanilla JS and CSS. If you're a wizard with modern UI frameworks (React, Vue, Svelte) or Tailwind CSS, we’d love to see a more robust and dynamic frontend.
- **Backend Refactoring**: The Django backend is currently very lightweight. Help us restructure the code to better align with standard REST API practices, perhaps migrating to FastAPI for lower latency and async support.
- **Packaging**: Help us optimize the PyInstaller build process to reduce the final `.app` size.

### 3. Report Bugs and Request Features
If you find a bug or have an idea for a cool new feature, please open an issue! 
- Be as detailed as possible. Include your OS, version, and the steps to reproduce the issue.
- If you're requesting a feature, explain *why* it would be useful and how it fits into the broader Antigravity ecosystem.

## Getting Started

1. **Fork the repository** and clone it locally.
2. Create your feature branch: `git checkout -b feature/my-new-feature`.
3. Set up the development environment by installing the requirements: `pip install -r requirements.txt`.
4. Make your changes and test them thoroughly.
5. Commit your changes: `git commit -am 'Add some feature'`.
6. Push to the branch: `git push origin feature/my-new-feature`.
7. Submit a **Pull Request**.

We look forward to building the future of autonomous quota management with you!
