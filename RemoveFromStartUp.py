import os
from readchar import readchar
import pyfiglet
import pyfiglet.fonts

AUTOSTART_PATH = os.path.expanduser('~') + r"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\AutoUpdater.lnk"
os.remove(AUTOSTART_PATH)

f = pyfiglet.Figlet(font='slant')
print(f.renderText('Ungoogled Chromium Autoupdater'))
print()
print("The Script Has Been Removed From The Startup!")
print("Press Any Key To Exit...")
readchar()