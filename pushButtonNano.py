import Jetson.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
inPin = 15
GPIO.setup(inPin, GPIO.IN)
inPin2 = 16
GPIO.setup(inPin2, GPIO.IN)
while True:
    x = GPIO.input(inPin)
    y = GPIO.input(inPin2)
    # time.sleep(1)
    print(f'Switch 1: {x}')
    print(f'Switch 2: {y}')
    time.sleep(1)

    
    