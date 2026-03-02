# Antigravity Model Reset Timer
**Master Project Descriptor & Integration Roadmap**

---

## 1. Project Overview
The **Antigravity Model Reset Timer** is a standalone, cross-platform desktop application designed to track and manage usage quotas for various Large Language Models (LLMs), currently supporting Gemini Flash, Gemini Pro, and Claude Opus/Sonnet. 

The application helps developers and prompt engineers keep track of their API rate limits, remaining request percentages, and exact timer resets, preventing unexpected service interruptions during heavy agentic workflows.

## 2. Current Architecture
The application is built using a hybrid web-to-native stack:
- **Backend (Python/Django)**: A lightweight Django server manages the data layer, utilizing an embedded SQLite database (`models.py` -> `AntigravityAccount`). It handles the time-delta math and calculates absolute UTC reset timestamps.
- **Frontend (HTML/Vanilla JS/CSS)**: A responsive, dark-mode dashboard rendered using standard web technologies. It uses Django's templating engine and custom template filters (`timer_extras.py`) to dynamically color-code remaining percentages.
- **Native GUI (`pywebview`)**: The web dashboard is wrapped in a native Cocoa window for macOS, hiding the underlying browser infrastructure.
- **Packaging (`PyInstaller`)**: The Python runtime, Django server, and webview module are frozen into a single `AntigravityTimer.app` bundle via a custom `launcher.py` entry point that safely forks the background server process.

---

## 3. Future Roadmap: Antigravity Ecosystem Integration

To evolve this tool from a manual tracker into a core component of the **Antigravity** autonomous AI ecosystem, the following enhancements should be considered:

### Phase 1: Automated Telemetry & API Polling
- **Direct Platform Hooks**: Instead of relying on manual user input, the application should securely store API keys and poll the respective provider endpoints (Google AI Studio, Anthropic Console) to automatically fetch remaining token quotas and rate limits in real-time.
- **Local Inter-Process Communication (IPC)**: Expose a lightweight local REST or WebSocket API that the main Antigravity agent can query to securely check its own "fuel levels" before initiating resource-intensive tasks.

### Phase 2: Agentic Fallback & Auto-Pausing
- **Smart Throttling**: If the timer app detects that an account's quota drops below a critical threshold (e.g., < 10%), it can send a signal to the running Antigravity agent.
- **Dynamic Model Switching**: The Antigravity agent reads the timer's signal and automatically falls back to a cheaper/faster model (e.g., switching from Opus to Flash) or safely pauses its workflow, entering a sleep state until the absolute UTC reset timestamp is reached.

### Phase 3: Transition to a Native Antigravity Extension
Ultimately, maintaining a standalone desktop window may introduce unnecessary overhead. The ideal end-state for this application is to become a native extension:
- **VS Code / IDE Extension**: Port the dashboard into a native VS Code Webview panel (since Antigravity heavily integrates with IDEs). This places the data directly alongside the developer's code.
- **Antigravity CLI Plugin**: Integrate the quota tracking logic directly into the Antigravity core library as a plugin module, allowing the AI to inherently understand its own rate limit constraints as a primary context variable without needing a separate visual dashboard.
