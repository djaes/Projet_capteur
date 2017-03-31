import os

def scan():
	os.system("sudo hciconfig hci0 down")
	os.system("sudo hciconfig hci0 up")
	os.system("sudo hcitool lescan> donnees/scan.txt & sleep 5 && sudo pkill --signal SIGINT hcitool")
