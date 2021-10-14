import time

import network
import urequests as requests


class Wifi:
    wlan = None
    SSID = "AmongstUsNet"
    PASSWORD = "AmongstUs"
    URL = "http://192.1.1.1:5000/"

    def __init__(self, parent):
        self.parent = parent
        # Initialize wlan object
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        # try to connect to the set wifi AP
        self.wlan.connect(self.SSID, self.PASSWORD)
        # Keep looping until connection is successful
        while True:
            if self.wlan.isconnected():
                print("Connected to: " + self.SSID)
                self.parent.screen.drawText("Connected", 0, 0)
                return
            else:
                time.sleep_ms(500)
                print("Connecting...")
                self.parent.screen.drawText("Connecting", 0, 0)
    def sendRequest(self, message):
        response = requests.get(self.URL+ message)
        print(self.URL+ message)
        text = response.text
        print(text)
        response.close()
        return(text)

    
