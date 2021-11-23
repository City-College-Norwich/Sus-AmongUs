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
                self.parent.screen.clear()
                self.parent.screen.drawText("Connected", 0, 0)
                self.parent.screen.draw()
                return
            else:
                time.sleep_ms(500)
                print("Connecting...")
                self.parent.screen.clear()
                self.parent.screen.drawText("Connecting", 0, 0)
    
    def sendRequest(self, message):
        class DepricatedException(Exception):
            pass
        try:
            raise DepricatedException("This function 'sendRequest' is Depricated please use the other general purpose functions outlined in WiFi.py",1.9)
        except Exception as e:
            print (repr(e))

    # Interal usage ONLY!
    def _sendRequest(self, message):
        response = requests.get(self.URL+ message)
        print(self.URL+ message)
        text = response.text
        print(text)
        response.close()
        return(text)
        
    def isAlive(self, tagID):
        if self._sendRequest("isAlive?badgeUID=" + tagID) == "yes":
            return True
        else:
            return False

    def completeMinigame(self, tagID):
        return self._sendRequest("minigameComplete?badgeUID=" + tagID)

    def startVoting(self, tagID):
        return self._sendRequest("startVote?badgeUID=" + tagID)

    def requestStation(self, tagID):
        return self._sendRequest("requestStation?badgeUID=" + tagID)

    def createSabotage(self, type):
        return self._sendRequest("sabotage?sabotageType=" + type)

    def completeSabotage(self,badgeUID):
        return self._sendRequest("sabotageCompleted?badgeUID=" + badgeUID)

    def registerUser(self, tagID):
        return self._sendRequest("registerUser?badgeUID=" + tagID)

    def startGame(self):
        return self._sendRequest('StartGame')

    def voteTally(self, badgeUID, myUID):
        return self._sendRequest("voteTally?badgeUID="+badgeUID+"&myUID="+myUID)

    def initiateVote(self):
        return self._sendRequest("initiateVote")

    def voteTimeEnd(self):
        return self._sendRequest("voteTimeEnd")

    def keepAlive(self):
        return self._sendRequest("keepAlive")

    def AutoDownloader(self):
        return self._sendRequest("AutoDownloader/GetFileList")

    def getTagName(self, uid):
        return self._sendRequest("getTagName?uid=" + uid)

    def killPlayer(self, myUID, victimUID):
        return self._sendRequest("killPlayer?myUID={}&victimUID{}".format(myUID, victimUID))

    def isImposter(self, uid):
        return self._sendRequest("isImposter?uid="+uid)

    def getFileList(self):
        return self._sendRequest("AutoDownloader/GetFileList")

    def getFile(self, filename):
        return self._sendRequest("AutoDownloader/GetFile?fileName="+filename)
    
