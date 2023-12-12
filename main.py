import keyboard as kb
import time

def press_keys():
    kb.press_and_release("5")
    time.sleep(1)
    kb.press_and_release("5")

def main():
    time.sleep(5)
    while True:
        press_keys()
        time.sleep(55)

if __name__ == '__main__':
    main()