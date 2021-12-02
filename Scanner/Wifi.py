import json
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
                
                self.parent.screen.drawText("Connecting", 0, 0)
                self.parent.screen.draw()
    
    def sendRequest(self, message):
        class DepricatedException(Exception):
            pass
        try:
            raise DepricatedException("This function 'sendRequest' is Depricated please use the other general purpose functions outlined in WiFi.py",1.9)
        except Exception as e:
            print (repr(e))

    # Interal usage ONLY!
    def _sendRequest(self, message: str) -> str:
        response = requests.get(self.URL+ message)
        print(self.URL+ message)
        text = response.text
        print(text)
        response.close()
        return(text)

    def isAlive(self, tagID: hex) -> bool:
        if self._sendRequest("isAlive?badgeUID=" + tagID) == "yes":
            return True
        else:
            return False

    def completeMinigame(self, tagID: hex) -> None:
        return self._sendRequest("minigameComplete?badgeUID=" + tagID)


    def startVoting(self) -> str:
        self._sendRequest("startVote")
        return "ok"
    

    def startEmergency(self) -> str:
        if bool(self._sendRequest("checkMeeting")):
            voteType='meeting'
            self._sendRequest("setVoteType?type=" + voteType)#so the server knows a vote has started from emergency meeting
            self._sendRequest("startVote")
        return "ok"

    
    def startReportBody(self) -> str:
        voteType='report'
        self._sendRequest("setVoteType?type=" + voteType)#so the server knows a vote has started from dead body reported
        self._sendRequest("startVote")
        return "ok"

    def requestStation(self, tagID: hex) -> str:
        return self._sendRequest("requestStation?badgeUID=" + tagID)

    def createSabotage(self, sabotageType: str) -> str:
        print ("Creating sabotage {}".format(sabotageType))
        return self._sendRequest("sabotage?sabotageType=" + sabotageType)

    def completeSabotage(self,badgeUID: hex) -> str:
        return self._sendRequest("sabotageCompleted?badgeUID=" + badgeUID)

    def registerUser(self, tagID) -> bool:
        returns = self._sendRequest("registerUser?badgeUID=" + tagID)
        if returns == "True":
            return True
        else:
            return False

    def startGame(self) -> str:
        return self._sendRequest('StartGame')

    def voteTally(self, badgeUID: hex, myUID: hex) -> str:
        return self._sendRequest("voteTally?badgeUID="+badgeUID+"&myUID="+myUID)

    def skipStation(self,lastStation):
        return self._sendRequest("skipStation?lastStation=" + lastStation)

    def joinVote(self,badgeUID: hex) -> str:
        return self._sendRequest("joinVote?badgeUID=" + badgeUID)

    def keepAlive(self) -> str:
        return self._sendRequest("keepAlive")

    def AutoDownloader(self) -> str:
        return self._sendRequest("AutoDownloader/GetFileList")

    def getTagName(self, uid: hex) -> str:
        return self._sendRequest("getTagName?uid=" + uid)

    def killPlayer(self, myUID: hex, victimUID: hex) -> str:
        return self._sendRequest("killPlayer?myUID={}&victimUID={}".format(myUID, victimUID))

    def isImposter(self, uid: hex) -> str:
        return self._sendRequest("isImposter?uid="+uid)

    def getFileList(self) -> str:
        return self._sendRequest("AutoDownloader/GetFileList")

    def getFile(self, filename: str) -> str:
        return self._sendRequest("AutoDownloader/GetFile?fileName="+filename)

    def getPlayers(self) -> dict:
        return json.loads(self._sendRequest("getPlayers"))

