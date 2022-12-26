import os
from readchar import readchar

AUTOSTART_PATH = os.path.expanduser('~') + r"\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\AutoUpdater.lnk"
os.remove(AUTOSTART_PATH)

print("The Script Has Been Removed From The Startup!")
print("Press Any Key To Exit...")
readchar()