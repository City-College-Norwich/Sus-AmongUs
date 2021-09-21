import mfrc522
from os import uname


class Rfid:
    def __init__(self):
        self.rdr = mfrc522.MFRC522(0, 1, 2, 3, 4)#Update Pins**
        
    def __update__(self):
        pass

    def do_read(self):
        (stat, tag_type) = self.rdr.request(rdr.REQIDL)

	if stat == self.rdr.OK:
            (stat, raw_uid) = self.rdr.anticoll()

	    if stat == self.rdr.OK:
                return "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            else:
                return None


