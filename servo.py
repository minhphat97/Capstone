import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

pwm=GPIO.PWM(3, 50)
pwm.start(0)

angle = 90
duty = angle / 18 + 2
GPIO.output(3, True)
pwm.CHangeDutyCycle(duty)
print("sleeping for 3s")
sleep(3)
GPIO.output(3, False)
pwm.ChangeDutyCycle(0)

angle = 45
duty = angle / 18 + 2
GPIO.output(3, True)
pwm.CHangeDutyCycle(duty)
print("sleeping for 3s")
sleep(3)
GPIO.output(3, False)
pwm.ChangeDutyCycle(0)

pwm.stop()
GPIO.cleanup()