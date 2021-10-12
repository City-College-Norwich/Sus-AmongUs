import time

import os
mode = os.environ.get("MODE")

DEBUG = False
if(mode == "DEBUG"):
    DEBUG = True
    import requests
else:
    import network
    import urequests as requests


class Wifi:
    wlan = None
    SSID = "AmongstUsNet"
    PASSWORD = "AmongstUs"
    URL = "http://192.1.1.1:5000/"

    def __init__(self):
        if(mode == "DEBUG"):
            print("WiFi Loading in Debug Mode")
            return;


        # Initialize wlan object
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        # try to connect to the set wifi AP
        self.wlan.connect(self.SSID, self.PASSWORD)
        # Keep looping until connection is successful
        while True:
            if self.wlan.isconnected():
                print("Connected to: " + self.SSID)
                return
            else:
                time.sleep_ms(500)
                print("Connecting...")
                
    def sendRequest(self, message):
        print("Requesting: " + self.URL+ message)
        if(DEBUG):
            r = requests.get(self.URL+ message)
            print (r.text)
            return (r.text)
        response = requests.get(self.URL+ message)
        print(self.URL+ message)
        text = response.text
        print(text)
        response.close()
        return(text)

    
