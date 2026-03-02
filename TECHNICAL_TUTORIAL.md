# How to Turn a local Django App into a Native Desktop GUI (Without Electron)

Electron is the default choice for desktop apps, but it comes with a heavy tax: hundreds of megabytes of overhead and high idle CPU usage. If you're building a simple utility—like a timer or a tracker—you don't need a whole browser instance running in the background.

In this tutorial, I’ll show you how I built **Antigravity-Model-Reset-Timer**, a native desktop app that uses **Django**, **PyWebView**, and **MongoDB** to achieve a 0% background CPU footprint.

## The Architecture: Target Timestamp

Most desktop timers use background loops. Antigravity-Model-Reset-Timer handles state differently:
1. **Backend (Django):** Calculates the absolute future expiration time in UTC.
2. **Database (MongoDB/Djongo):** Stores that fixed timestamp.
3. **Frontend (Vanilla JS/PyWebView):** When the window is open, it calculates the `delta` between the DB and the OS hardware clock.

This means you can close the app entirely, and your timer "stays alive" without consuming a single cycle.

## Step 1: The Launcher Script

The secret sauce is `launcher.py`. Instead of the user running `python manage.py runserver`, we wrap the Django process and the GUI in a single execution point.

```python
import webview
import subprocess
import sys
import time

def start_server():
    # Start Django invisibly in the background
    return subprocess.Popen(
        [sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000', '--noreload'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

if __name__ == '__main__':
    server = start_server()
    time.sleep(1.5) # Wait for Django to bind
    
    # Launch the native OS window pointing to localhost
    webview.create_window('Antigravity Timer', 'http://127.0.0.1:8000')
    webview.start()
    
    server.terminate() # Cleanup on exit
```

## Step 2: Persistence with Djongo

We use `djongo` to bridge Django's ORM with MongoDB. This allows us to store complex account limits and timers as simple documents without sacrificing the power of Django's models.

```python
# models.py
from django.db import models

class AccountTimer(models.Model):
    name = models.CharField(max_length=100)
    target_utc = models.DateTimeField() # This is the anchor
```

## Step 3: The "Zero-Drain" Frontend

In your template, use simple JavaScript to render the countdown. Since the logic is based on the difference between `now` and `target_utc`, the UI remains perfectly synced even after a computer restart.

```javascript
const targetTime = new Date("{{ timer.target_utc|date:'c' }}").getTime();
setInterval(() => {
    const now = new Date().getTime();
    const distance = targetTime - now;
    // Update DOM...
}, 1000);
```

## Why This Wins

1. **Lightweight:** No Chromium overhead.
2. **Robust:** If the app crashes, the timer doesn't care. Absolute time is absolute.
3. **Developer-Friendly:** You get to use the full power of the Django ecosystem (Auth, Admin, ORM) for a local desktop tool.

---

**Antigravity-Model-Reset-Timer** is fully open-source. Fork it on GitHub, add some API webhooks, and help us build a lighter desktop ecosystem!

[Insert Repo Link Here]
