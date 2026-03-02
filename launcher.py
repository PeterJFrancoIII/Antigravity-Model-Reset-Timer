import webview
import subprocess
import sys
import time
import os
import multiprocessing

# Global variable to hold our background Django process
django_process = None

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def start_server():
    """Starts the Django development server invisibly in the background."""
    global django_process
    
    # We use subprocess.Popen to run the server without blocking the main thread
    # stdout and stderr are routed to DEVNULL to keep your Mac terminal clean
    if getattr(sys, 'frozen', False):
        cmd = [sys.executable, 'runserver', '127.0.0.1:8000', '--noreload']
    else:
        cmd = [sys.executable, resource_path('manage.py'), 'runserver', '127.0.0.1:8000', '--noreload']

    django_process = subprocess.Popen(
        cmd,
        cwd=resource_path(".")
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
    multiprocessing.freeze_support()
    
    # Check if we're spawned as a subprocess to run the Django server
    if getattr(sys, 'frozen', False) and len(sys.argv) > 1 and sys.argv[1] == 'runserver':
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'antigravity_timer.settings')
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
        sys.exit(0)

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
