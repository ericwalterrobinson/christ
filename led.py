import RPi.GPIO as GPIO
import time
greenPins = [17, 18, 27]
redPins = [20, 21]
allPins = [17, 18, 27, 20, 21]
def setup():
   # Set the GPIO modes to BCM Numbering
   GPIO.setmode(GPIO.BCM)
   # Set LedPin's mode to output,and initial level to High(3.3v)
   #GPIO.setup(redPins, GPIO.OUT, initial=GPIO.LOW)
   GPIO.setup(allPins, GPIO.OUT, initial=GPIO.HIGH)
# Define a main function for main process
def main():
   GPIO.output(redPins, GPIO.HIGH)
   while True:
      #print ('...LED ON')
      # Turn on LED
      GPIO.output(greenPins, GPIO.LOW)
      GPIO.output(redPins, GPIO.HIGH)
      time.sleep(0.5)
      #print ('LED OFF...')
      # Turn off LED
      GPIO.output(redPins, GPIO.LOW)
      GPIO.output(greenPins, GPIO.HIGH)
      time.sleep(0.5)
# Define a destroy function for clean up everything after the script finished
def destroy():
   # Turn off LED
   GPIO.output(greenPins, GPIO.HIGH)
   # Release resource
   GPIO.cleanup()
# If run this script directly, do:
if __name__ == '__main__':
   setup()
   try:
      main()
   # When 'Ctrl+C' is pressed, the program destroy() will be  executed.
   except KeyboardInterrupt:
      destroy()