import os
from win32com.client import Dispatch
from readchar import readchar

PATH = os.path.dirname(os.path.realpath(__file__))
AUTOSTART_PATH = os.path.expanduser('~') + r"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\AutoUpdater.lnk"
TARGET_PATH = os.path.join(PATH, "main.exe")

print(AUTOSTART_PATH)

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(AUTOSTART_PATH)
shortcut.Targetpath = TARGET_PATH
shortcut.WorkingDirectory = PATH
shortcut.save()

print("The Script Has Been Added To The Startup!")
print("Press Any Key To Exit...")
readchar()