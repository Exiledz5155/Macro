import pydirectinput
from pynput import mouse
import time
import json

def execute_macro(macro):
    print("Macro activated!")

    for key, t in macro:
        pydirectinput.keyDown(key)
        elapsed_time = time.time() - t
        time.sleep(max(0.01 - elapsed_time, 0))  # Ensure a minimum delay between key presses
        pydirectinput.keyUp(key)

def playback_macro(macro):
    print("Playing back the macro...")

    start_time = time.perf_counter()

    for key, t in macro:
        elapsed_time = time.perf_counter() - start_time
        target_time = t + elapsed_time

        pydirectinput.keyDown(key)
        current_time = time.perf_counter()

        while current_time < target_time:
            current_time = time.perf_counter()

        pydirectinput.keyUp(key)

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.x1:
        try:
            with open("macro.json", "r") as f:
                loaded_macro = json.load(f)
            playback_macro(loaded_macro)
        except Exception as e:
            print(f"Error loading or playing back macro: {e}")

# Main program
if __name__ == "__main__":
    print("The program is running. Click the back button of the mouse (Mouse 4) to activate the macro.")

    with mouse.Listener(on_click=on_click) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            pass
