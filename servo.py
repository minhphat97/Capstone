import RPi.GPIO as GPIO
import time

# setup RPi
GPIO.setwarnings(False)
servo_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin,GPIO.OUT)

# 50 Hz or 20 ms PWM period
# 2.90 A on 7.4V
pwm = GPIO.PWM(servo_pin,50) 

print("Starting at zero...")
pwm.start(5) 

try:
    while True:
        print("Setting to zero...")
        angle = 0
        duty = angle / 27 + 2
        pwm.ChangeDutyCycle(duty) 
        time.sleep(3)

        print("Setting to 180...")
        angle = 180 
        duty = angle / 27 + 2
        pwm.ChangeDutyCycle(duty) 
        time.sleep(3)

        print("Setting to 90...")
        angle = 90
        duty = angle / 27 + 2
        pwm.ChangeDutyCycle(duty) 
        time.sleep(3)

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