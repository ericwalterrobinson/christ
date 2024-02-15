import RPi.GPIO as GPIO
import time
import sys

greenPins = [17, 18, 27]
redPins = [20, 21]
allPins = [17, 18, 27, 20, 21]
orderedPins = [17, 21, 18, 20, 27]
def setup():
   # Set the GPIO modes to BCM Numbering
   GPIO.setmode(GPIO.BCM)
   # Set LedPin's mode to output,and initial level to High(3.3v)
   GPIO.setup(allPins, GPIO.OUT, initial=GPIO.HIGH)

def switchState(pin):
   #print(1 if GPIO.input(pin) == 0 else 0)
   return 1 if GPIO.input(pin) == 0 else 0

def rollingStateForTime(pins, duration):
   if type(pins) is list:
      for pin in pins:
         GPIO.output(pin, switchState(pin)) #switches the high/low state
   else:
      GPIO.output(pins, switchState(pins))
   time.sleep(duration)

def blinkForTime(pins, duration):
   if type(pins) == list:
      for pin in pins:
         print(pin, switchState(pin))
         GPIO.output(pin, switchState(pin))
      time.sleep(duration)
      for pin in pins:
         GPIO.output(pin, switchState(pin))
   else:
      GPIO.output(pins, switchState(pins))
      time.sleep(duration)
      GPIO.output(pins, switchState(pins))

def main():
   if len(sys.argv) == 2:
      if sys.argv[1] == "loop":
         GPIO.output(redPins, GPIO.HIGH)
         GPIO.output(greenPins, GPIO.LOW)
         while True:
            blinkForTime(allPins, 0.5)
            #print ('...LED ON')
            # Turn on LED
            #GPIO.output(greenPins, GPIO.LOW)
            #GPIO.output(redPins, GPIO.HIGH)
            #time.sleep(0.5)
            #print ('LED OFF...')
            # Turn off LED
            #GPIO.output(redPins, GPIO.LOW)
            #GPIO.output(greenPins, GPIO.HIGH)
            #time.sleep(0.5)
      elif sys.argv[1] == "roll":
         while True:
            for pin in orderedPins:
               rollingStateForTime(pin, 0.2)
               #GPIO.output(pin, GPIO.LOW)
               #time.sleep(0.2)
               #GPIO.output(pin, GPIO.HIGH)
      elif sys.argv[1] == "row":
         while True:
            for pin in orderedPins:
               blinkForTime(pin, 0.2)

   else:
      print("What am I supposed to do with the LEDs?")




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
