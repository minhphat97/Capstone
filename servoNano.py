from adafruit_servokit import ServoKit
import time
servo_pin = 0
kit = ServoKit(channels=16)
kit.servo[servo_pin].angle=0
print("Angle is 0")
time.sleep(3)
kit.servo[servo_pin].angle=90
print("Angle is 90")
time.sleep(3)
kit.servo[servo_pin].angle=180
print("Angle is 180")
time.sleep(3)

# import time
# from adafruit_servokit import ServoKit

# # Configure PCA9685
# kit = ServoKit(channels=16)

# # Servo calibration values
# servo_min = 150  # Minimum servo pulse length
# servo_max = 600  # Maximum servo pulse length

# # Function to control the servo position
# def set_servo_position(channel, angle):
#     pulse_length = servo_min + (servo_max - servo_min) * angle // 180
#     kit.servo[channel].angle = pulse_length

# # Move the servo to different angles
# set_servo_position(0, 0)   # Move servo on channel 0 to 0 degrees
# time.sleep(1)
# set_servo_position(0, 90)  # Move servo on channel 0 to 90 degrees
# time.sleep(1)
# set_servo_position(0, 180) # Move servo on channel 0 to 180 degrees
# time.sleep(1)

# # Cleanup
# kit.servo[0].angle = None  # Release the servo