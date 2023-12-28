import pydirectinput
from pynput import mouse

# Set the delay between key presses and releases
pydirectinput.PAUSE = 0.01

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.x1:
        print("Macro activated!")

        keys_to_press = ['1', '2', '4', '5']

        for key in keys_to_press:
            pydirectinput.keyDown(key)

        for key in keys_to_press:
            pydirectinput.keyUp(key)

# Main program
if __name__ == "__main__":
    print("The program is running. Click the back button of the mouse (Mouse 4) to activate the macro.")

    with mouse.Listener(on_click=on_click) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            pass
