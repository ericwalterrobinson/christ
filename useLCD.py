from lcd import LCD
from time import sleep
import subprocess
import sys


	
def main():
	global lcd
	lcd = LCD()
	lcd.clear()
	lcd.message("Welcome to --->\n  CLS TECH")
	sleep(5)
	lcd.clear()
	if sys.argv & len(sys.argv) == 1:
		lcd.message(sys.argv[0])
	elif sys.argv:
		for msg in sys.argv:
			lcd.message(msg)
			sleep(5)
			lcd.clear()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		lcd.clear()
		lcd.destroy()