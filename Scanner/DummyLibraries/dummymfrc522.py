class MFRC522:
    OK = 0
    FAILED = 2

    def __init__(self, sck, mosi, miso, rst, sda):
        print ("RFID dummy module created")

    def request(self, a, b):
        return (self.FAILED, None)

    def anticoll(self):
        return (self.FAILED, None)