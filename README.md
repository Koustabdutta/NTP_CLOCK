# ⏰ Raspberry Pi Pico W NTP Clock with I2C LCD (PCF8574)

This project displays real-time NTP-synced clock data on a 16x2 LCD using a Raspberry Pi Pico W and PCF8574 I2C backpack. The clock automatically connects to Wi-Fi, fetches accurate time from an NTP server, and displays it in HH:MM:SS format.

---

## 🛠️ Features

- Real-time NTP time sync
- Displays date and time on 16x2 LCD
- I2C communication via PCF8574
- Supports time zone offset (e.g. IST: UTC+5:30)
- Clean MicroPython implementation

---

## 📦 Hardware Used

| Component            | Quantity |
|---------------------|----------|
| Raspberry Pi Pico W | 1        |
| 16x2 I2C LCD (PCF8574) | 1     |
| Breadboard & wires   | As needed |

---

## 🔌 Circuit Diagram

| LCD Pin | PCF8574 | Pico W GPIO | Notes     |
|---------|---------|-------------|-----------|
| VCC     |         | 3.3V        | Power     |
| GND     |         | GND         | Ground    |
| SDA     |         | GP4         | I2C SDA   |
| SCL     |         | GP5         | I2C SCL   |

---

## 🧠 Software Requirements

- [Thonny IDE](https://thonny.org/)
- MicroPython firmware for Raspberry Pi Pico W
- Files to upload:
  - `main.py`
  - `lcd_api.py`
  - `i2c_lcd.py`

---

## 🚀 Getting Started

1. Flash MicroPython to your Pico W.
2. Clone or download this repository.
3. Open `main.py` in Thonny.
4. Replace `your_SSID` and `your_PASSWORD` with your Wi-Fi credentials.
5. Upload all three files to the Pico W.
6. Run the code and view the time on the LCD!

---

## 🌐 Time Zone Configuration

To adjust for your time zone:
```python
TIME_OFFSET = 5.5 * 3600  # For IST (UTC+5:30)
