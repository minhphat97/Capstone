# #! /usr/bin/python
# import RPi.GPIO as GPIO
# import time

# while True:
#     try:
#         GPIO.setmode(GPIO.BOARD)

#         PIN_TRIGGER = 7
#         PIN_ECHO = 11

#         GPIO.setup(PIN_TRIGGER, GPIO.OUT)
#         GPIO.setup(PIN_ECHO, GPIO.IN)

#         GPIO.output(PIN_TRIGGER, GPIO.LOW)
#         print("Waiting for sensor to settle")
#         time.sleep(2)

#         print("Calculating distance")
#         GPIO.output(PIN_TRIGGER, GPIO.HIGH)
#         time.sleep(0.00001)
#         GPIO.output(PIN_TRIGGER, GPIO.LOW)

#         while GPIO.input(PIN_ECHO) == 0:
#             pulse_start_time = time.time()
#         while GPIO.input(PIN_ECHO) == 1:
#             pulse_end_time = time.time()

#         pulse_duration = pulse_end_time - pulse_start_time
#         distance = round(pulse_duration * 34300 * 0.5)
#         print("Distance (cm): ", distance)

#     finally:
#         GPIO.cleanup()

#! /usr/bin/python
import RPi.GPIO as GPIO
import time

PIN_TRIGGER = 7
PIN_ECHO = 11
PIN_TRIGGER2 = 18
PIN_ECHO2 = 24
PIN_TRIGGER3 = 23
PIN_ECHO3 = 26

while True:
    try:
        GPIO.setmode(GPIO.BOARD)
        # PIN_TRIGGER3 

        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)
        GPIO.setup(PIN_TRIGGER2, GPIO.OUT)
        GPIO.setup(PIN_ECHO2, GPIO.IN)
        GPIO.setup(PIN_TRIGGER3, GPIO.OUT)
        GPIO.setup(PIN_ECHO3, GPIO.IN)

        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        GPIO.output(PIN_TRIGGER2, GPIO.LOW)
        GPIO.output(PIN_TRIGGER3, GPIO.LOW)
        print("Waiting for sensor 1 to settle")
        # time.sleep(2)

        print("Waiting for sensor 2 to settle")
        print("Waiting for sensor 3 to settle")
        time.sleep(3)

        print("Calculating distance 1")
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO) == 0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 34300 * 0.5)
        print("Distance 1 (cm): ", distance)

        print("Calculating distance 2")
        GPIO.output(PIN_TRIGGER2, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER2, GPIO.LOW)

        while GPIO.input(PIN_ECHO2) == 0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO2) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance2 = round(pulse_duration * 34300 * 0.5)
        print("Distance 2 (cm): ", distance2)

        print("Calculating distance 3")
        GPIO.output(PIN_TRIGGER3, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER3, GPIO.LOW)

        while GPIO.input(PIN_ECHO3) == 0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO3) == 1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance3 = round(pulse_duration * 34300 * 0.5)
        print("Distance 3 (cm): ", distance3)

    finally:
        GPIO.cleanup()