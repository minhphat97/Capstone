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
Look at [Service-Information](objectPiservice-Information.md) to set up the Pi to run its program on start.
On the laptop, run 
```bash
python3 objectLaptop.py
```
**after** the Pi has started up. Make sure a webcam is connected to the laptop and the Pi has the appropriate connections to the servo.