import os
from time import time
from configparser import ConfigParser
  
configur = ConfigParser()
configur.read('config.ini')

LastCheckedForUpdate = configur.getint("info", "LastCheckedForUpdate")
UpdateInvervall = configur.getint("settings", "LookForUpdateEvery")
configur.set('info','LastCheckedForUpdate', str(int(time())))

with open('config.ini', 'w') as config:
    configur.write(config)

if (time() - LastCheckedForUpdate) > UpdateInvervall:
    os.system("start python updater.py")