import RPi.GPIO as GPIO
import time

# setup RPi
GPIO.setwarnings(False)
servo_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

# 50 Hz or 20 ms PWM period
pwm = GPIO.PWM(servo_pin,50) 

print("Starting at zero...")
pwm.start(5) 

try:
    while True:
        print("Setting to zero...")
        pwm.ChangeDutyCycle(5) 
        time.sleep(15)

        print("Setting to 180...")
        pwm.ChangeDutyCycle(10) 
        time.sleep(15)

        print("Setting to 90...")
        pwm.ChangeDutyCycle(7.5) 
        time.sleep(15)
except KeyboardInterrupt:
    pwm.stop() 
    GPIO.cleanup()
    print("Program stopped")




# import RPi.GPIO as GPIO
# import time

# servoPIN = 17
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(servoPIN, GPIO.OUT)

# p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
# p.start(2.5) # Initialization

# angle = 90
# duty = angle / 18 + 2
# GPIO.output(servoPIN, True)
# p.ChangeDutyCycle(0)
# p.ChangeDutyCycle(duty)
# print("sleeping for 15s")
# time.sleep(15)
# p.ChangeDutyCycle(0)
# GPIO.output(servoPIN, False)
# print("already back to angle of 0 degree and waiting 50s")
# time.sleep(50)

# angle = 90
# duty = angle / 18 + 2
# GPIO.output(servoPIN, True)
# p.ChangeDutyCycle(0)
# p.ChangeDutyCycle(duty)
# print("sleeping for 15s")
# time.sleep(15)
# p.ChangeDutyCycle(0)
# GPIO.output(servoPIN, False)


# p.stop()
# GPIO.cleanup()

# import RPi.GPIO as GPIO
# import time

# servoPIN = 17
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(servoPIN, GPIO.OUT)

# p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
# p.start(2.5) # Initialization
# try:
#   while True:
#     p.ChangeDutyCycle(5)
#     time.sleep(0.5)
#     p.ChangeDutyCycle(7.5)
#     time.sleep(0.5)
#     p.ChangeDutyCycle(10)
#     time.sleep(0.5)
#     p.ChangeDutyCycle(12.5)
#     time.sleep(0.5)
#     p.ChangeDutyCycle(10)
#     time.sleep(0.5)
#     p.ChangeDutyCycle(7.5)
#     time.sleep(0.5)
#     p.ChangeDutyCycle(5)
#     time.sleep(0.5)
#     p.ChangeDutyCycle(2.5)
#     time.sleep(0.5)
# except KeyboardInterrupt:
#   p.stop()
#   GPIO.cleanup()