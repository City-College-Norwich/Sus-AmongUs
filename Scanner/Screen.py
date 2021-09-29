#Among Us Screen

from machine import Pin, I2C
import ssd1306, time

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
        self.updateOccured = False
        
    def display_text(self, text, x_coordinate, y_coordinate):
        self.updateOccured = True
        self.display.text(text, x_coordinate, y_coordinate)

    def display_rectangle(self, x_coordinate, y_coordinate, width, height):
        self.updateOccured = True
        self.display.fillRect(x_coordinate, y_coordinate, width, height)
        pass
        
    def clear_screen(self):
        self.updateOccured = True
        self.display.fill(0)
        
    def draw_screen(self):
        if self.updateOccured:
            self.display.show()
            self.updateOccured = False

    def update(self):
        pass

    def fill(self, value):
        self.firstCheck()
        if value == 1:
            self.display.fill(1)
        elif value == 0:
            self.display.fill(0)
            
if self.updateOccured = False:
            self.clear_screen()
