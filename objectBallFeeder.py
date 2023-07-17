import time
from adafruit_servokit import ServoKit
import keyboard
import board
import busio
servo_pin = 12
i2c=board.I2C()
i2c=busio.I2C(board.SCL_1,board.SDA_1) # this is i2c 0
kit = ServoKit(channels=16,i2c=i2c)

#angle = 30
print("STARTING")
kit.servo[servo_pin].angle = 90
while True:
    if keyboard.is_pressed("f"):
        #ngle = 60
        kit.servo[servo_pin].angle = 120
        print ("120")
        time.sleep(0.33)
        #angle = 30
        #print (angle)
        kit.servo[servo_pin].angle = 90
        time.sleep(3)
        print("DELAY OVER")
    #print (angle)




