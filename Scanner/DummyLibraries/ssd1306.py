# MicroPython SSD1306 OLED driver, I2C and SPI interfaces

class SSD1306():
    def __init__(self, width, height, external_vcc):
        return;

    def init_display(self):
        return;

    def poweroff(self):
        return;

    def poweron(self):
        return;

    def contrast(self, contrast):
        return;

    def invert(self, invert):
        return;

    def rotate(self, rotate):
        return;

    def show(self):
        return;


class SSD1306_I2C(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3C, external_vcc=False):
        return;

    def write_cmd(self, cmd):
        return;

    def write_data(self, buf):
        return;


class SSD1306_SPI(SSD1306):
    def __init__(self, width, height, spi, dc, res, cs, external_vcc=False):
        return;

    def write_cmd(self, cmd):
        return;

    def write_data(self, buf):
        return;
