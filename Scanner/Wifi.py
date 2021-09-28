import time

import network
import urequests as requests


class Wifi:
    wlan = None
    SSID = "woodnet"
    PASSWORD = "CCNRules"
    URL = "http://localhost:5000s/"

    def __init__(self):
        # Initilize wlan object
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        # try to connect to the set wifi AP
        self.wlan.connect(self.SSID, self.PASSWORD)
        # Keep looping until connection is successful
        while True:
            if self.wlan.isconnected():
                return
            else:
                time.sleep_ms(500)

    def sendRequest(self, message):
        response = requests.get(URL+"/"+message)
        response.close()
        return response.text
