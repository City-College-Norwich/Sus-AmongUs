class MFRC522:
    OK = 0
    FAILED = 2
    def init__(self, a, b, c, d, e):
        print ("RFID dummy module created")

    def request(self, a, b):
        return (self.FAILED, None)

    def anticoll(self):
        return (self.FAILED, None)