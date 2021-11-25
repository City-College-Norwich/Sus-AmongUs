import ssd1306
from machine import Pin, I2C

import time


class Screen:
    def __init__(self):
        resetPin = Pin(16, Pin.OUT)
        resetPin.value(0)
        time.sleep_ms(5)
        resetPin.value(1)

        scl = Pin(15, Pin.OUT, Pin.PULL_UP)
        sda = Pin(4, Pin.OUT, Pin.PULL_UP)
        i2c = I2C(scl=scl, sda=sda)
        self.display = ssd1306.SSD1306_I2C(128, 64, i2c)
        self.updateOccurred = False

    def drawText(self, text, x_coordinate=0, y_coordinate=0):
        self.clearScreen()
        self.display.text(text, x_coordinate, y_coordinate)

    def drawRectangle(self, x_coordinate, y_coordinate, width, height):
        self.clearScreen()
        self.display.fill_rect(x_coordinate, y_coordinate, width, height, 1)

    def clear(self):
        self.clearScreen()
        self.fill(0)

    def draw(self):
        if self.updateOccurred:
            self.display.show()
            self.updateOccurred = False

    def update(self):
        pass

    def fill(self, value):
        if value == 1:
            self.display.fill(1)
        elif value == 0:
            self.display.fill(0)

    def clearScreen(self):
        if self.updateOccurred == False:
            self.fill(0)
            self.updateOccurred = True
