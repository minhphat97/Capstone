#!/usr/bin/env bash
python3 objectBallFeeder.py &
python3 objectBallNano.py &
python3 PID_control.py 
# The user interface will run after the above programs are terminated
python3 template.py
