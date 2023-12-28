import pydirectinput
from pynput import mouse
import time


def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.x1:
        print("Macro activated!")

        for key in ['1', '2', '4', '5']:
            pydirectinput.keyDown(key)

        time.sleep(0.01)

        for key in ['1', '2', '4', '5']:
            pydirectinput.keyUp(key)


# Main program
if __name__ == "__main__":
    print("The program is running. Click the back button of the mouse (Mouse 4) to activate the macro.")

    with mouse.Listener(on_click=on_click) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            pass
