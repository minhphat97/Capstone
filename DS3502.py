from time import sleep
import board
import adafruit_ds3502

i2c = board.I2C()  # uses board.SCL and board.SDA
ds3502 = adafruit_ds3502.DS3502(i2c)

# As this code runs, measure the voltage between ground and the RW (wiper) pin
# with a multimeter. You should see the voltage change with each print statement.
for i in range (0, 127, 5):
    ds3502.wiper = i
    print("Wiper value set to ", i)
    sleep(3.0)
print("SETTING WIPER TO 0")
ds3502.wiper = 0
