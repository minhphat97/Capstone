import time
#from adafruit_servokit import ServoKit
import keyboard
# import board
# import busio
# servo_pin = 4
# i2c=board.I2C()
# i2c=busio.I2C(board.SCL_1,board.SDA_1) # this is i2c 0
# kit = ServoKit(channels=16,i2c=i2c)

angle = 30
# kit.servo[servo_pin].angle = 30
while True:
    if keyboard.is_pressed("f"):
        angle = 60
        # kit.servo[servo_pin].angle = 60
        print (angle)
        time.sleep(0.5)
        angle = 30
        # kit.servo[servo_pin].angle = 30
    print (angle)


