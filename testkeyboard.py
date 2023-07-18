import evdev
from evdev import InputDevice, categorize, ecodes


devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
touchscreen_keyboard_path = None

for device in devices:
    print(device.path, device.name)
    if "HID 27c0:0818" in device.name:
        touchscreen_keyboard_path = device.path
        touchscreen_keyboard = device
        break

if touchscreen_keyboard_path is None:
    print("Touchscreen keyboard not found")
    exit(1)

device = evdev.InputDevice(touchscreen_keyboard.fn)


for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY: 
        key_event = evdev.categorize(event)
        if key_event.keystate == key_event.key_down and key_event.keycode[0] == 'KEY_F':
            print("F is pressed")

        