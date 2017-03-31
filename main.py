import time
import os
from donnees.get_config_ini import Get_config_ini
from process.filtrage import filtrage
from process.scan import scan

timer = {}
config = Get_config_ini()
os.system("sudo systemctl daemon-reload")
os.system("sudo service bluetooth restart")
os.system("sudo hciconfig hci0 up")

while 1:
    try:
        print("debut du scan")
        scan()
        print("debut du filtrage")
        timer = filtrage(config, timer)
    except KeyboardInterrupt:
        print ('Scan stopé')
        os.system("sudo hciconfig hci0 down")
        break        
