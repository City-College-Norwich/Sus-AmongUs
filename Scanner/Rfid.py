import mfrc522
from TimerHelper import TimerHelper
class Rfid:

    def __init__(self):
        self.rdr = mfrc522.MFRC522(12, 2, 17, 0, 13)
        self.timer = TimerHelper()
        self.timer.Set(100)
        self.timerSet = False

    def update(self):
        pass

    def do_read(self):

        if self.timer.Check():
            self.timer.Set(100)
            (stat, tag_type) = self.rdr.request(self.rdr.REQIDL)

            if stat == self.rdr.OK:
                (stat, raw_uid) = self.rdr.anticoll()   
                if stat == self.rdr.OK:
                    uid= "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                    self.name = self.parent.wifi.send_request('getTagName?uid=' + uid )
                    return self.name
                    
            # if anything failed set name to none
            self.name = None    

        # send previous result while timer hasnt been hit
        return self.name


