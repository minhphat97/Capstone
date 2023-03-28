# from gpiozero import MotionSensor

# pir = MotionSensor(4)

# while True:
#     print("On")
#     pir.wait_for_motion()
#     # pir.wait_for_active()
#     print("You moved")
#     pir.wait_for_no_motion()

# Works but is slow

# import RPi.GPIO as GPIO
# import time

# GPIO.setmode(GPIO.BCM)
# PIR_PIN = 4
# GPIO.setup(PIR_PIN, GPIO.IN)

# try:
#     print("PIR Module Test")
#     time.sleep(2)
#     print("Ready")
#     while True:
#         if GPIO.input(PIR_PIN):
#             print("1")
#         else:
#             print("0")
#         # time.sleep(1)
# except KeyboardInterrupt:
#     print ("Quit")
#     GPIO.cleanup()

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR_PIN = 4
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
    print ("Motion Detected!")

print("PIR Module Test (CTRL+C to exit)")
time.sleep(2)
print ("Ready")

try:
    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
    while 1:
        time.sleep(1)
except KeyboardInterrupt:
    print ("Quit")
    GPIO.cleanup()