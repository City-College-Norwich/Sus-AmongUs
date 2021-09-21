import network
import time

class Wifi:
    wlan = None
    SSID = "woodnet"
    PASSWORD = "CCNRules"
    def __init__(self):
        # Initilize wlan object
        if(self.wlan == None):
            self.wlan = network.WLAN(network.STA_IF)
            self.wlan.active(True)
        # try to connect to the set wifi AP
        self.wlan.connect(self.SSID,self.PASSWORD)
        # Keep looping until connection is successful
        while True:
            if self.wlan.isconnected():
                return
            else:
                time.sleep_ms(500)
