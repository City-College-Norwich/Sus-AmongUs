import mfrc522


class Rfid:
    def __init__(self):
        self.rdr = mfrc522.MFRC522(12, 2, 17, 0, 13)
        
    def update(self):
        pass

    def do_read(self):
        (stat, tag_type) = self.rdr.request(self.rdr.REQIDL)

        if stat == self.rdr.OK:
            (stat, raw_uid) = self.rdr.anticoll()   

            if stat == self.rdr.OK:
                return "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
            else:
                return None


