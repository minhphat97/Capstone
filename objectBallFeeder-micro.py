
import time
from adafruit_servokit import ServoKit
import keyboard
import board
import busio
import socket

servo_pin = 12
i2c=board.I2C()
i2c=busio.I2C(board.SCL_1,board.SDA_1) # this is i2c 0
kit = ServoKit(channels=16,i2c=i2c)

#angle = 30
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Accept connections from any port
ip = ""
port = 12346

# Connect to the laptop's IP address and port
# sock.bind((ip, port))
print("Connected to laptop at", (ip, port))
sock.bind((ip, port))
sock.listen(1)  # Listen for incoming connections, with a backlog of 1 connection
conn, addr = sock.accept()  # Accept an incoming connection

print("STARTING BALL FEEDER COMPONENT")
kit.servo[servo_pin].angle = 90
while True:
    print("INSIDE LOOP")
    data_received = conn.recv(4096)
    data_received = data_received.decode()
    if not data_received:
        kit.servo[servo_pin].angle = 90
        print("ERROR: BALL FEEDER TURNING OFF")
        break
    
    try:
        distance, rot_angle, wiper, launch_ball= map(float, data_received.split(','))
        if launch_ball is 1:
            #ngle = 60
            kit.servo[servo_pin].angle = 120
        #  print ("120")
            time.sleep(0.352)
            #angle = 30
            #print (angle)
            kit.servo[servo_pin].angle = 90
            time.sleep(3)
            print("DELAY OVER")
            
        elif launch_ball is 2:
            kit.servo[servo_pin].angle = 90
            print("BALL FEEDER TURNING OFF")
            break
    except ValueError as e:
        print("Error while parsing data:", e)
        
    #print (angle)

conn.close()
sock.close()




