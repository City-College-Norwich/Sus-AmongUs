#Among Us Screen

from machine import Pin, I2C
import ssd1306

class Screen:
    def __init__(self):
        i2c = I2C(sda=Pin(0), scl=Pin(1)) #Fix Pins
        self.display = ssd1306.SSD1306_I2C(128, 64, i2c)

    def display_text(self, text, x_coordinate, y_coordinate):
        self.display.text(text, x_coordinate, y_coordinate)
        
    def clear_screen(self):
        self.display.fill(0)
        
    def draw_screen(self):
        self.display.show()

    def update(self):
        pass

    def fill(self, value):
        if value == 1:
            self.display.fill(1)
        elif value == 0:
            self.display.fill(0)
