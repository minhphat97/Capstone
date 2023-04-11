# Made by IronFoot Technologies
This file explains how to run the KickPro project

## Downloading Packages
The project requires both a laptop capable of running Linux and a Raspberry Pi.

The following packages should be downloaded on the laptop:
- numpy
- opencv-python
- pickle

The following packages should be downloaded on the Pi
- pickle
- RPi.GPIO
The RPi.GPIO should come built-in for the Pi.

## Downloading Code
To download the code and use the correct branch, run the following commands on both the laptop and pi:
```bash
git clone https://github.com/minhphat97/Capstone.git
git checkout linux-version2
```

## Running Code
SSH into the Pi using PuTTY. The hostname should be ```raspberrypi.local```, the port ```22```, and the connection type ```SSH```. Both the laptop and the Pi should be on the same network. For the demonstration, we are using the mobile hotspot ```SM-Company3```. 
On the laptop, first open objectLaptop.py then make sure
```python
host = "192.168.210.151"
```
is the IP address of the Pi. The address can change on startup, so make sure it's correct. The IP address can be found in the mobile hotspot settings or by running
```bash
ifconfig
```
on the Pi. Afterwards, run
```bash
python3 objectPi.py
```
Then run 
```bash
python3 objectLaptop.py
```
Make sure it is **after** the program on the Pi is running. Also ensure a webcam is connected to the laptop and the Pi has the appropriate connections to the servo.

## Extra (In The Future)
Look at [Service-Information](objectPiservice-Information.md) to set up the Pi to run its program on start.
