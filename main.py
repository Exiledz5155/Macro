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

    print(f"Pressing and releasing key 5 with {round(press_release_1 * 100, 2)} ms delay.")
    kb.press("5")
    time.sleep(press_release_1)
    kb.release("5")

    print(f"Pausing for {round(sleep_time, 2)} seconds.")
    time.sleep(sleep_time)

    print(f"Pressing and releasing key 5 with {round(press_release_2 * 100, 2)} ms delay.")
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

    files_in_directory = os.listdir(script_dir)

    mp3_files = [file for file in files_in_directory if file.lower().endswith(".mp3")]

    if mp3_files:
        # Play the first mp3 file
        mp3_to_play = os.path.join(script_dir, mp3_files[0])
    else:
        print("No mp3 files found in the script directory.")

    while True: # TODO add hotkey function
        if mp3_files:
            # Play the first mp3 file
            mp3_to_play = os.path.join(script_dir, mp3_files[0])
            print(f"Playing {mp3_to_play}")
            ply(mp3_to_play)
        else:
            print("No mp3 files found in the script directory.")

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

