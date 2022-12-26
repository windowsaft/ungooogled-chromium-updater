import os
from win32com.client import Dispatch
from readchar import readchar
import pyfiglet
import pyfiglet.fonts

PATH = os.getcwd()
AUTOSTART_PATH = os.path.expanduser('~') + r"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\AutoUpdater.lnk"
TARGET_PATH = os.path.join(PATH, "AutoUpdater.exe")

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(AUTOSTART_PATH)
shortcut.Targetpath = TARGET_PATH
shortcut.WorkingDirectory = PATH
shortcut.save()

f = pyfiglet.Figlet(font='slant')
print(f.renderText('Ungoogled Chromium Autoupdater'))
print()
print("The Script Has Been Added To The Startup!")
print("Press Any Key To Exit...")
readchar()