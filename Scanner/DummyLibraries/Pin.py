class Pin:
    OK = 0
    FAILED = 2

    def __init__(self, sck, d):
        print ("Pin module created")

    def request(self, a, b):
        return (self.FAILED, None)

    def anticoll(self):
        return (self.FAILED, None)