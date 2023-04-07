import RPi.GPIO as GPIO
import socket
import pickle
import time

servo_pin = 17
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)
print("Starting at 100...")
pwm.start(5)

angle = 100  # set angle Servo
duty = angle / 27 + 2
pwm.ChangeDutyCycle(duty)

# Socket setup
host = ""  # Empty string means the server will accept connections on any available network interface
port = 12345  # Choose the same unique port number as in the laptop code
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)  # Listen for incoming connections, with a backlog of 1 connection
conn, addr = s.accept()  # Accept an incoming connection

while True:
    try:
        data = conn.recv(4096)
        if data:
            values = pickle.loads(data)
            x_medium = values["x_medium"]
            center = values["center"]

            if x_medium < center - 30:
                if angle >= 140:
                    angle = 140
                    duty = angle / 27 + 2
                    pwm.ChangeDutyCycle(duty)
                else:
                    angle = angle + 1
                    duty = angle / 27 + 2
                    pwm.ChangeDutyCycle(duty)
            elif x_medium > center + 30:
                if angle <= 40:
                    angle = 40
                    duty = angle / 27 + 2
                    pwm.ChangeDutyCycle(duty)
                else: 
                    angle = angle - 1
                    duty = angle / 27 + 2
                    pwm.ChangeDutyCycle(duty)
            else:
                angle = angle
                duty = angle / 27 + 2
                pwm.ChangeDutyCycle(duty)

            print("Servo Angle is: ", angle)
            print("Human Center is: ", x_medium)
            print("Frame Center is: ", center)
            print()

    except KeyboardInterrupt:
        angle = 90
        duty = angle / 27 + 2
        pwm.ChangeDutyCycle(duty)
        print("")
        print("**************************************************************")
        print("Shutting down")
        print("**************************************************************")
        print("")
        break

conn.close()
s.close()
pwm.stop()
GPIO.cleanup()
       
