# Made by IronFoot Technologies

This file explains how to run the KickPro project
## Downloading Packages

The project requires both a laptop capable of running Linux and a Raspberry Pi.

The following packages should be downloaded on the laptop:

* numpy
* opencv-python
* time
* socket
* keyboard

The following packages should be downloaded on the Nano
* ServoKit
* busio
* keyboard
* board
* time
* adafruit_ds3502
* socket
* Jetson.GPIO


The Jetson.GPIO should come built-in for the Jetson.

## Downloading Code

To download the code and use the correct branch, run the following commands on both the laptop and Nano:

```bash
git clone https://github.com/minhphat97/Capstone.git
git checkout UsingLaptop
```

## Running Code

Turn on the JetsonNano. The appropriate scripts should run from launch.

Then navigate to the terminal on the laptop and launch the VM Workstation and the 'Demo' VM. The appropraite scripts should launch automatically

Make sure it is after the program on the Nano is running. Also ensure the webcams are connected and there is an ethernet connection between the laptop and nano.
