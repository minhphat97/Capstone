import Jetson.GPIO as GPIO
import time

# setup RPi
GPIO.setwarnings(False)
servo_pin = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

# 50 Hz or 20 ms PWM period
# 2.90 A on 7.4V with lab power supply
# 135 degrees will be treated as our zero
# With power supply, we are using 8.4 V and unknown amps
pwm = GPIO.PWM(servo_pin,50) 

print("Starting at zero...")
pwm.start(5) 

try:
    while True:
        print("Setting to 100...")
        angle = 100
        duty = angle / 27 + 2
        pwm.ChangeDutyCycle(duty) 
        time.sleep(3)

        # print("Setting to 120...")
        # angle = 120
        # duty = angle / 27 + 2
        # pwm.ChangeDutyCycle(duty) 
        # time.sleep(3)

        # print("Setting to 100...")
        # angle = 100
        # duty = angle / 27 + 2
        # pwm.ChangeDutyCycle(duty) 
        # time.sleep(3)

except KeyboardInterrupt:
    pwm.stop() 
    GPIO.cleanup()
    print("Program, stopped")
