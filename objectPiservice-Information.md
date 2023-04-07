# ObjectPi.service

This is a copy of the objectPi.service file in the Pi for reference. 

## Code

The /etc/systemd/system/objectpi.service file in the Pi contains the following lines:
```bash
[Unit]
Description=Run objectPi.py on startup
After=multi-user.target

[Service]
User=pi
WorkingDirectory=/home/pi/Capstone/
ExecStart=/usr/bin/python3 /home/pi/Capstone/objectPi.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

## Enable and disable
To enable the service on startup, run in terminal
```bash 
$ sudo systemctl enable objectpi.service
```
To disable the service, run in terminal 
```bash
$ sudo systemctl disable objectpi.service
 ```
Afterwards reboot the Pi to test the script. It can also be done in terminal
```bash
sudo reboot
```
