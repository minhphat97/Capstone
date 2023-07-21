#!/usr/bin/env bash
# sudo python3 /home/jg26/Capstone/PID_control-laptop.py &
# sudo python3 /home/jg26/Capstone/objectBallNano-laptop.py # &
# sudo python3 /jg26/ironfoot/Capstone/PID_control.py #&
cleanup() {
    echo "Cleaning up..."
    sudo fuser -k 12345/tcp  # This will forcibly kill the process using port 12345
}

# Trap the EXIT signal and call the cleanup function
trap cleanup EXIT

cd Capstone
sudo ./run-micro.sh
cd ..
echo "ALL DONE"
exit 0

# MOVE TO HOME DIRECTORY OF NANO
# ENABLE WITH $ sudo chmod +x start-micro.sh
# ALSO ENABLE IN THE CAPSTONE DIRECTORY $ sudo chmod +x run-micro.sh
