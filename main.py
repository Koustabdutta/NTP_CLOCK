# main.py
import network
import ntptime
import time
from machine import Pin, I2C
from i2c_lcd import I2cLcd

# Replace with your Wi-Fi
ssid = 'your_SSID'
password = 'your_PASSWORD'

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Connecting to WiFi...", end="")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(1)
print("\nConnected:", wlan.ifconfig())

# Sync time with NTP
try:
    ntptime.settime()
except:
    print("Failed to sync time")

# Add UTC offset (e.g., +5.5 hours for IST)
TIME_OFFSET = 5.5 * 3600

# LCD setup (I2C0 with SDA=GP4, SCL=GP5)
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)  # Change 0x27 to your LCD's address if needed

lcd.clear()
lcd.putstr("   NTP CLOCK")

# Main loop
while True:
    t = time.localtime(time.time() + int(TIME_OFFSET))
    lcd.move_to(0, 1)
    lcd.putstr("{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
        t[1], t[2], t[3], t[4], t[5]
    ))
    time.sleep(1)
