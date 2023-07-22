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

## Running Code (Test)

Turn on the Jetson Nano. On the laptop, launch VM Workstation and the 'Demo' VM. The password is `ironfoot` for the duration of the demo. Make sure both devices are connected to the same wifi network. 

Edit the IP address variable in `test-micro.py` on the Nano to be the IP address of the laptop. Edit the IP address variable in `test-laptop.py` on the laptop to be the IP address of the Nano. Use either the nano editor (`nano <file>`) or open an IDE (`code-oss` on the Nano, `code .` on the laptop).

The IP address of a device can be determined by running `sudo ifconfig` in the terminal of that device. Alternatively, if both devices are connected to a mobile hotspot, the IP addresses can be determined in the wifi settings there. The laptop can ping the nano consistently (command is `ping <ip_address of other device>`), though not vice versa. That is ok. The scripts can run fine even if the ping from the Nano to the laptop hangs.

Open the terminal on the Nano. Run `sudo python3 test-micro.py`. *Then* on the laptop, run `sudo python3 test-laptop.py`

Make sure `test-laptop.py` runs after the program on the Nano is running. Also ensure the webcam is connected to the laptop.
