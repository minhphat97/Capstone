#!/usr/bin/env bash
sudo python3 /home/ironfoot/Capstone/objectBallFeeder.py &
sudo python3 /home/ironfoot/Capstone/objectBallNano.py &
sudo python3 /home/ironfoot/Capstone/PID_control.py 
# The user interface will run after the above programs are terminated
sudo python3 /home/ironfoot/Capstone/userInterface.py
