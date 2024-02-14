import pigpio
from time import sleep
servo = 19


pwm = pigpio.pi()

pwm.set_servo_pulsewidth(servo, 1600)


sleep(3)

pwm.set_servo_pulsewidth(servo, 1300)

sleep(3)

pwm.set_servo_pulsewidth(servo, 1500)
