from adafruit_servokit import ServoKit
import time
servo_pin = 0
kit = ServoKit(channels=16)
while True:
    # kit.servo[servo_pin].angle=0
    # print("Angle is 0")
    # time.sleep(3)
    i = 90 # angle
    direction = 0 # 0 is positive, 1 is negative
    step = 10 # change in angle
    while True:
        kit.servo[servo_pin].angle=i
        result = f'Angle is {i}'
        print(result)
        time.sleep(1)
        if i >= 180:
            direction = 1
        elif i <= 0:
            direction = 0
        
        if direction == 0:
            i = i + step
        elif direction >= 1:
            i = i - step

    # kit.servo[servo_pin].angle=5
    # print("Angle is 5")
    # time.sleep(3)
    # kit.servo[servo_pin].angle=10
    # print("Angle is 10")
    # time.sleep(3)
    # kit.servo[servo_pin].angle=15
    # print("Angle is 15")
    # time.sleep(3)
    # kit.servo[servo_pin].angle=20
    # print("Angle is 20")
    # time.sleep(3)
    # kit.servo[servo_pin].angle=25
    # print("Angle is 25")
    # time.sleep(3)
    # kit.servo[servo_pin].angle=90
    # print("Angle is 90")
    # time.sleep(3)
    # kit.servo[servo_pin].angle=180
    # print("Angle is 180")
    # time.sleep(3) 

# # import time
# # from adafruit_servokit import ServoKit
# # import Jetson.GPIO as GPIO

# # # Configure PCA9685
# # kit = ServoKit(channels=16)

# # # Servo calibration values
# # servo_min = 150  # Minimum servo pulse length
# # servo_max = 600  # Maximum servo pulse length

# # # Function to control the servo position
# # import Jetson.GPIO as GPIO
# # import time
# # import Adafruit_PCA9685

# # pwm = Adafruit_PCA9685.PCA9685()
# # pwm.set_pwm_frequecy(50)

# # servo_min = 150
# # servo_max = 600

# # def set_servo_position(channel, angle):
# #     pulse_length = servo_min + (servo_max - servo_min) * angle // 180
# #     pwm.set_pwm(channel, 0 , pulse_length)

# # set_servo_position(0, 0)
# # time.sleep(1)
# # set_servo_position(0, 90)
# # time.sleep(1)
# # set_servo_position(0, 180)
# # time.sleep(1)

# # pwm.set_all_pwm(0, 0)
# import Jetson.GPIO as GPIO
# # import time
# # import Adafruit_PCA9685

# # pwm = Adafruit_PCA9685.PCA9685()
# # pwm.set_pwm_frequecy(50)

# # servo_min = 150
# # servo_max = 600

# # def set_servo_position(channel, angle):
# #     pulse_length = servo_min + (servo_max - servo_min) * angle // 180
# #     pwm.set_pwm(channel, 0 , pulse_length)

# # set_servo_position(0, 0)
# # time.sleep(1)
# # set_servo_position(0, 90)
# # time.sleep(1)
# # set_servo_position(0, 180)
# # time.sleep(1)

# # pwm.set_all_pwm(0, 0)
# import Jetson.GPIO as GPIO
# # import time
# # import Adafruit_PCA9685

# # pwm = Adafruit_PCA9685.PCA9685()
# # pwm.set_pwm_frequecy(50)

# # servo_min = 150
# # servo_max = 600

# # def set_servo_position(channel, angle):
# #     pulse_length = servo_min + (servo_max - servo_min) * angle // 180
# #     pwm.set_pwm(channel, 0 , pulse_length)

# # set_servo_position(0, 0)
# # time.sleep(1)
# # set_servo_position(0, 90)
# # time.sleep(1)
# # set_servo_position(0, 180)
# # time.sleep(1)

# # pwm.set_all_pwm(0, 0)
# import Jetson.GPIO as GPIO
# # import time
# # import Adafruit_PCA9685

# # pwm = Adafruit_PCA9685.PCA9685()
# # pwm.set_pwm_frequecy(50)

# # servo_min = 150
# # servo_max = 600

# # def set_servo_position(channel, angle):
# #     pulse_length = servo_min + (servo_max - servo_min) * angle // 180
# #     pwm.set_pwm(channel, 0 , pulse_length)

# # set_servo_position(0, 0)
# # time.sleep(1)
# # set_servo_position(0, 90)
# # time.sleep(1)
# # set_servo_position(0, 180)
# # time.sleep(1)

# # pwm.set_all_pwm(0, 0)
# # pwm = Adafruit_PCA9685.PCA9685()
# # pwm.set_pwm_frequecy(50)

# # servo_min = 150
# # servo_max = 600

# # def set_servo_position(channel, angle):
# #     pulse_length = servo_min + (servo_max - servo_min) * angle // 180
# #     pwm.set_pwm(channel, 0 , pulse_length)

# # set_servo_position(0, 0)
# # time.sleep(1)
# # set_servo_position(0, 90)
# # time.sleep(1)
# # set_servo_position(0, 180)
# # time.sleep(1)

# # pwm.set_all_pwm(0, 0)
# # import Jetson.GPIO as GPIO
# # import time
# # import Adafruit_PCA9685

# # pwm = Adafruit_PCA9685.PCA9685()
# # pwm.set_pwm_frequecy(50)

# # servo_min = 150
# # servo_max = 600

# # def set_servo_position(channel, angle):
# #     pulse_length = servo_min + (servo_max - servo_min) * angle // 180
# #     pwm.set_pwm(channel, 0 , pulse_length)

# # set_servo_position(0, 0)
# # time.sleep(1)
# # set_servo_position(0, 90)
# # time.sleep(1)
# # set_servo_position(0, 180)
# # time.sleep(1)

# # pwm.set_all_pwm(0, 0)vo_min) * angle // 180
# import Jetson.GPIO as GPIO
# # import time
# # import Adafruit_PCA9685

# # pwm = Adafruit_PCA9685.PCA9685()
# # pwm.set_pwm_frequecy(50)

# # servo_min = 150
# # servo_max = 600

# # def set_servo_position(channel, angle):
# #     pulse_length = servo_min + (servo_max - servo_min) * angle // 180
# #     pwm.set_pwm(channel, 0 , pulse_length)

# # set_servo_position(0, 0)
# # time.sleep(1)
# # set_servo_position(0, 90)
# # time.sleep(1)
# # set_servo_position(0, 180)
# # time.sleep(1)

# # pwm.set_all_pwm(0, 0)
# import Jetson.GPIO as GPIO
# # import time
# # import Adafruit_PCA9685

# # pwm = Adafruit_PCA9685.PCA9685()
# # pwm.set_pwm_frequecy(50)

# # servo_min = 150
# # servo_max = 600

# # def set_servo_position(channel, angle):
# #     pulse_length = servo_min + (servo_max - servo_min) * angle // 180
# #     pwm.set_pwm(channel, 0 , pulse_length)

# # set_servo_position(0, 0)
# # time.sleep(1)
# # set_servo_position(0, 90)
# # time.sleep(1)
# # set_servo_position(0, 180)
# # time.sleep(1)

# # pwm.set_all_pwm(0, 0)
# # # Move the servo to different angles
# # set_servo_position(0, 0)   # Move servo on channel 0 to 0 degrees
# # time.sleep(1)
# # set_servo_position(0, 90)  # Move servo on channel 0 to 90 degrees
# # time.sleep(1)
# # set_servo_position(0, 180) # Move servo on channel 0 to 180 degrees
# # time.sleep(1)

# # # Cleanup
# # kit.servo[0].angle = None  # Release the servo

# # import Jetson.GPIO as GPIO
# # import time
# # import Adafruit_PCA9685

# # pwm = Adafruit_PCA9685.PCA9685()
# # pwm.set_pwm_frequecy(50)

# # servo_min = 150
# # servo_max = 600

# # def set_servo_position(channel, angle):
# #     pulse_length = servo_min + (servo_max - servo_min) * angle // 180
# #     pwm.set_pwm(channel, 0 , pulse_length)

# # set_servo_position(0, 0)
# # time.sleep(1)
# # set_servo_position(0, 90)
# # time.sleep(1)
# # set_servo_position(0, 180)
# # time.sleep(1)

# # pwm.set_all_pwm(0, 0)
# # GPIO.setwarnings(False)
# # servo_pin = 13
# # GPIO.setmode(GPIO.BCM)
# # GPIO.setup(servo_pin,GPIO.OUT)

# # pwm = GPIO.PWM(servo_pin,50) 

# # print("Starting at zero...")
# # pwm.start(5) 

# # try:
# #     while True:
# #         print("Setting to zero...")
# #         angle = 0
# #         duty = angle / 27 + 2
# #         pwm.ChangeDutyCycle(duty) 
# #         time.sleep(3)

# #         print("Setting to 180...")
# #         angle = 180
# #         duty = angle / 27 + 2
# #         pwm.ChangeDutyCycle(duty)  
# #         time.sleep(3)

# #         print("Setting to 90...")
# #         angle = 90
# #         duty = angle / 27 + 2
# #         pwm.ChangeDutyCycle(duty) 
# #         time.sleep(3)

# # except KeyboardInterrupt:
# #     pwm.stop() 
# #     GPIO.cleanup()
# #     print("Program stopped")