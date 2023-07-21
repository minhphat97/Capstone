#!/usr/bin/env bash
cleanup() {
    echo "Cleaning up..."
    sudo fuser -k 12345/tcp  # This will forcibly kill the process using port 12345
}

# Trap the EXIT signal and call the cleanup function
trap cleanup EXIT

sudo python3 /home/ironfoot/Capstone/objectBallFeeder.py &
sudo python3 /home/ironfoot/Capstone/objectBallNano-laptop.py &
sudo python3 /home/ironfoot/Capstone/PID_control.py #&
