import mfrc522
from TimerHelper import TimerHelper


class Rfid:

    def __init__(self, parent):
        self.name = None
        self.rdr = mfrc522.MFRC522(26, 27, 14, 33, 25)
        self.timer = TimerHelper()
        self.timer.set(100)
        self.timerSet = False
        self.parent = parent
        print("Initiate Rfid")


    def update(self):
        pass

    def do_read(self):

        if self.timer.check():
            self.timer.set(100)
            (stat, tag_type) = self.rdr.request(self.rdr.REQIDL)

            if stat == self.rdr.OK:
                (stat, raw_uid) = self.rdr.anticoll()
                if stat == self.rdr.OK:
                    uid = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                    self.name = self.parent.wifi.send_request('getTagName?uid='+uid)
                    return self.name

            # if anything failed set name to none
            self.name = None

        # send previous result while timer hasnt been hit
        if self.name != None:
          print(self.name)
        return self.name
