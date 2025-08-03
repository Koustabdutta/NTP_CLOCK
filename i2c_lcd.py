# i2c_lcd.py
from lcd_api import LcdApi
from machine import I2C
import time

class I2cLcd(LcdApi):
    # Commands
    LCD_CLR = 0x01
    LCD_HOME = 0x02
    LCD_ENTRYMODESET = 0x04
    LCD_DISPLAYCONTROL = 0x08
    LCD_FUNCTIONSET = 0x20

    # Flags
    LCD_ENTRYLEFT = 0x02
    LCD_DISPLAYON = 0x04
    LCD_2LINE = 0x08
    LCD_5x8DOTS = 0x00

    ENABLE = 0b00000100
    RW = 0b00000010
    RS = 0b00000001

    def __init__(self, i2c, addr, num_lines=2, num_columns=16):
        self.i2c = i2c
        self.addr = addr
        self.num_lines = num_lines
        self.num_columns = num_columns
        self.backlight = 0x08

        time.sleep_ms(50)
        self._write_init(0x30)
        time.sleep_ms(5)
        self._write_init(0x30)
        time.sleep_ms(1)
        self._write_init(0x30)
        self._write_init(0x20)

        self._write_cmd(self.LCD_FUNCTIONSET | self.LCD_2LINE | self.LCD_5x8DOTS)
        self._write_cmd(self.LCD_DISPLAYCONTROL | self.LCD_DISPLAYON)
        self._write_cmd(self.LCD_ENTRYMODESET | self.LCD_ENTRYLEFT)
        self.clear()

        super().__init__(num_lines, num_columns)

    def _write_byte(self, data):
        self.i2c.writeto(self.addr, bytes([data | self.backlight]))

    def _pulse(self, data):
        self._write_byte(data | self.ENABLE)
        time.sleep_us(500)
        self._write_byte(data & ~self.ENABLE)
        time.sleep_us(500)

    def _write_init(self, data):
        self._write_byte(data)
        self._pulse(data)

    def _write_cmd(self, cmd):
        self._write_nibble(cmd & 0xF0)
        self._write_nibble((cmd << 4) & 0xF0)

    def _write_data(self, data):
        self._write_nibble(data & 0xF0, True)
        self._write_nibble((data << 4) & 0xF0, True)

    def _write_nibble(self, nibble, char_mode=False):
        mode = self.RS if char_mode else 0
        self._write_byte(nibble | mode)
        self._pulse(nibble | mode)

    def clear(self):
        self._write_cmd(self.LCD_CLR)
        time.sleep_ms(2)

    def move_to(self, col, row):
        row_offsets = [0x00, 0x40]
        self._write_cmd(0x80 | (col + row_offsets[row]))

    def putstr(self, string):
        for char in string:
            self._write_data(ord(char))
