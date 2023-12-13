import keyboard as kb
import time
import os
from playsound import playsound as ply
import ctypes, sys
import shutil
import random

# script_dir = getattr(sys, '_MEIPASS5', os.path.dirname(os.path.realpath(sys.argv[0])))
# bat_path = os.path.join(script_dir, 'sendKeys.bat')
#
# temp_bat_path = os.path.join(os.environ['TEMP'], 'sendKeys.bat')
# shutil.copyfile(bat_path, temp_bat_path)

script_dir = os.path.dirname(os.path.abspath(sys.executable))

bat_path = os.path.join(script_dir, 'sendKeys.bat')

def press_keys():
    press_release_1 = random.uniform(0.22, 0.89)
    press_release_2 = random.uniform(0.22, 0.89)
    sleep_time = random.uniform(.93, 1.52)

    print("Macro starting...")
    os.system(f'call {bat_path} "Warframe" ""')
    time.sleep(1)

    print(f"Pressing and releasing key 5 with {press_release_1 * 100} ms delay.")
    kb.press("5")
    time.sleep(press_release_1)
    kb.release("5")

    print(f"Pausing for {sleep_time} seconds.")
    time.sleep(sleep_time)

    print(f"Pressing and releasing key 5 with {press_release_2 * 100} ms delay.")
    kb.press("5")
    time.sleep(press_release_2)
    kb.release("5")

    print("Macro finished.")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    # os.chdir(r'C:\Users\Exiledz\PycharmProjects\Macro\dist')
    # print("Playing start.mp3")
    # ply('./start.mp3')
    while True: # TODO add hotkey function
        print("Playing start.mp3")
        ply('./start.mp3')
        press_keys()

        reset_timer = random.uniform(27.33, 49.56)

        time.sleep(reset_timer)

if __name__ == '__main__':
    if is_admin():
        print("Is Admin, proceeding:")
        main()
    else:
        print("Not Admin, permission will be asked.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

