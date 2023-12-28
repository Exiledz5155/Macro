import keyboard
import time

# Flag to keep track of whether the macro is active
macro_active = False

def start_stop_macro():
    global macro_active

    if not macro_active:
        # Start macro
        print("Macro started. Press Alt+F to stop.")
        keyboard.press("'")
        macro_active = True
    else:
        # Stop macro
        keyboard.release("'")
        print("Macro stopped.")
        macro_active = False

# Register hotkey Alt+F to start/stop the macro
keyboard.add_hotkey('alt+f', start_stop_macro)

# Keep the program running
try:
    keyboard.wait('esc')  # Press 'esc' to exit the program
except KeyboardInterrupt:
    pass
finally:
    # Release the key if the program is terminated
    if macro_active:
        keyboard.release("'")
