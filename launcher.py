import webview
import subprocess
import sys
import time
import os

# Global variable to hold our background Django process
django_process = None

def start_server():
    """Starts the Django development server invisibly in the background."""
    global django_process
    
    # We use subprocess.Popen to run the server without blocking the main thread
    # stdout and stderr are routed to DEVNULL to keep your Mac terminal clean
    django_process = subprocess.Popen(
        [sys.executable, 'manage.py', 'runserver', '127.0.0.1:8000', '--noreload'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

def on_closed():
    """Fires when the user clicks the red X on the native Mac window."""
    print("Native window closed. Terminating Antigravity background services...")
    if django_process:
        django_process.terminate()
        django_process.wait() # Ensure the process has fully exited
    print("Shutdown complete.")
    sys.exit(0)

if __name__ == '__main__':
    print("Starting Antigravity Timer Engine...")
    start_server()
    
    # Give Django 1.5 seconds to fully bind to the port before rendering the UI
    time.sleep(1.5)
    
    # Create the native OS window
    # Width and height are pre-optimized for our 3-column CSS grid
    window = webview.create_window(
        title='Antigravity Account Tracker',
        url='http://127.0.0.1:8000',
        width=1100,
        height=850,
        resizable=True,
        frameless=False
    )
    
    # Bind the cleanup function to the window closing event
    window.events.closed += on_closed
    
    # Launch the native UI
    webview.start()
