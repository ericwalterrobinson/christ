from lcd import LCD
from time import sleep
import subprocess

def getIP():
	addresses = subprocess.check_output("hostname -I", shell=True)
	ipAddr = addresses.decode("utf-8").split()[0]
	if(ipAddr):
		return ipAddr
	else:
		return "0.0.0.0"
	
def main():
	
	lcd = LCD()

	lcd.clear()
	lcd.message("Welcome to --->\n  CLS TECH")
	sleep(5)
	lcd.clear()
	lcd.message(getIP())