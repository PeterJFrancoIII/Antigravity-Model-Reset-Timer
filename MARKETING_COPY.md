# Marketing Strategy & Social Copy

## Section 1: Hacker News / r/Python (Text Post)
**Title:** Show HN: A Django-powered desktop timer with zero background CPU drain

I was tired of Electron-based tools eating 10% of my CPU just to track my Claude/GPT API limits. So I built **Antigravity-Model-Reset-Timer**.

It uses a "Target Timestamp Architecture." Instead of background loops, the Django backend stores absolute UTC expiration times in MongoDB. The PyWebView GUI calculates the delta against the OS clock only when visible. 

It’s cross-platform (Mac/Win/Linux), crash-proof (state persists in Mongo), and the entire core is under 10 files. 

Check it out: [Insert Repo Link]

---

## Section 2: X / Twitter Thread (4-part)

**Tweet 1:**
Building cross-platform desktop apps usually means one thing: Electron bloat. 

I wanted something different for my LLM limit tracker. 

Introducing **Antigravity-Model-Reset-Timer**. 🪐

Python + Django + PyWebView.

Ultra-smart. Ultra-simple. 🧵

**Tweet 2:**
The "Target Timestamp Architecture" 💡

No background loops.
No CPU drain. 
No battery murder. 🔋

Django calculates the UTC expiration. The vanilla JS GUI calculates the delta against your hardware clock. Simple, crash-proof, and lightweight.

**Tweet 3:**
Why Django for a Desktop App? 
- Built-in ORM for complex state. 
- Massive ecosystem. 
- MongoDB integration via Djongo. 

We wrapped it in PyWebView to get native performance without the 200MB overhead of Chromium. [Insert Screenshot]

**Tweet 4:**
V1.2 is officially Open Source. 🚀

We need your help building connectors for Anthropic, Google, and OpenAI webhooks. 

Repo here: [Insert Repo Link]

Let's build the leanest tool for the LLM era. 🪐
