# 🪐 Antigravity-Model-Reset-Timer

A lightweight, cross-platform desktop application built for Mac, Windows, and Linux to track LLM API limits with surgical precision and zero background resource drain.

## 🚀 The Architecture: Target Timestamp
Most timer apps rely on persistent background loops or cron jobs that eat CPU cycles and drain laptop batteries. **Antigravity-Model-Reset-Timer** flips the script with a "Target Timestamp Architecture":

1.  **Backend (Django):** Calculates the absolute future expiration time in UTC and stores it in MongoDB.
2.  **Frontend (Vanilla JS):** When the GUI is active, it calculates the delta between the stored timestamp and the OS hardware clock.

**The Result:** Zero background CPU drain. Your timers persist perfectly across reboots because they are anchored to absolute time, not relative loops. This is the Electron alternative the Python community has been waiting for.

## 🛠 Tech Stack
- **Python:** Core logic and orchestration.
- **Django:** Robust backend for state management.
- **MongoDB (via Djongo):** Lightning-fast document storage.
- **PyWebView:** Native OS window wrapper (avoiding Electron bloat).
- **Vanilla JS/HTML:** Premium, reactive UI without framework overhead.

## ⚡ Quick Start

### 1. Prerequisites
- **MacOS:** Use Homebrew to install MongoDB: `brew tap mongodb/brew && brew install mongodb-community@7.0`
- **Windows/Linux:** Download the standard MongoDB Community Server installer.

### 2. Setup
```bash
# Clone the repository
git clone https://github.com/PeterJFrancoIII/Antigravity-Model-Reset-Timer.git
cd Antigravity-Model-Reset-Timer

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Launch the application
python3 launcher.py
```

## 🤝 Call for Contributors!
**We are actively looking for developers to help evolve this project into a native extension of the autonomous Antigravity AI ecosystem!**

Whether you are a Python wizard, a frontend maestro, or an agentic builder, we need your help to implement:
- **Automated API Telemetry**: Direct hooks into Google AI Studio and Anthropic to poll quotas.
- **Agentic Polling**: Local REST/WebSocket IPC so autonomous agents can read their own "fuel levels" and pause workflows when quotas run low.
- **Native Extension Ports**: Migrating this dashboard into a VS Code extension or Antigravity CLI plugin.

👉 **Ready to build the future of AI tooling?** Check out our [Contribution Guidelines (CONTRIBUTING.md)](CONTRIBUTING.md) to get started.

### Existing Areas for Help
- **Webhooks:** Build API connectors for Anthropic, Google Gemini, and OpenAI.
- **Notifications:** Implement native OS desktop alerts for timer expirations.
- **Distributions:** Help refine the PyInstaller `.spec` builds for single-binary releases.

## 🏷️ Tags
#python #django #pywebview #desktop-app #electron-alternative #mongodb #llm-tools
