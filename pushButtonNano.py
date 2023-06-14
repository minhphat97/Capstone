import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
inPin = 15
GPIO.setup(inPin, GPIO.IN)
while True:
    x = GPIO.input(inPin)
    print(x)
    