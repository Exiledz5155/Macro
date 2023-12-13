import keyboard as kb
import time
import os
from playsound import playsound as ply
import ctypes, sys
import shutil

# script_dir = getattr(sys, '_MEIPASS5', os.path.dirname(os.path.realpath(sys.argv[0])))
# bat_path = os.path.join(script_dir, 'sendKeys.bat')
#
# temp_bat_path = os.path.join(os.environ['TEMP'], 'sendKeys.bat')
# shutil.copyfile(bat_path, temp_bat_path)

script_dir = os.path.dirname(os.path.abspath(sys.executable))

bat_path = os.path.join(script_dir, 'sendKeys.bat')

def press_keys():
    print("Macro running")
    os.system(f'call {bat_path} "Warframe" ""')
    time.sleep(1)
    kb.press_and_release("5")
    time.sleep(1)
    kb.press_and_release("5")
    print("Macro ended")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def main():
    # os.chdir(r'C:\Users\Exiledz\PycharmProjects\Macro\dist')
    # print("Playing start.mp3")
    # ply('./start.mp3')
    while True:
        print("Playing start.mp3")
        ply('./start.mp3')
        press_keys()
        time.sleep(52)

if __name__ == '__main__':
    if is_admin():
        print("Is Admin, proceeding:")
        main()
    else:
        print("Not Admin, permission will be asked.")
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

