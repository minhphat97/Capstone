# import RPi.GPIO as GPIO
# from time import sleep

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(3, GPIO.OUT)

# pwm=GPIO.PWM(3, 50)
# pwm.start(0)

# angle = 90
# duty = angle / 18 + 2
# GPIO.output(3, True)
# pwm.ChangeDutyCycle(duty)
# print("sleeping for 3s")
# sleep(3)
# GPIO.output(3, False)
# pwm.ChangeDutyCycle(0)

# angle = 45
# duty = angle / 18 + 2
# GPIO.output(3, True)
# pwm.ChangeDutyCycle(duty)
# print("sleeping for 3s")
# sleep(3)
# GPIO.output(3, False)
# pwm.ChangeDutyCycle(0)

# pwm.stop()
# GPIO.cleanup()

import RPi.GPIO as GPIO
import time

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
try:
  while True:
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(10)
    time.sleep(0.5)
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    p.ChangeDutyCycle(5)
    time.sleep(0.5)
    p.ChangeDutyCycle(2.5)
    time.sleep(0.5)
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()