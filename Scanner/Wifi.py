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
        print ("--- wifi")
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
                self.parent.screen.draw()
                return
            else:
                time.sleep_ms(500)
                print("Connecting...")
                
                self.parent.screen.drawText("Connecting", 0, 0)
    
    def sendRequest(self, message):
        print ("--- sendrequest")
        class DepricatedException(Exception):
            pass
        try:
            raise DepricatedException("This function 'sendRequest' is Depricated please use the other general purpose functions outlined in WiFi.py",1.9)
        except Exception as e:
            print (repr(e))

    # Interal usage ONLY!
    def _sendRequest(self, message):
        print ("--- sendrequest")
        response = requests.get(self.URL+ message)
        print(self.URL+ message)
        text = response.text
        print(text)
        response.close()
        return(text)
        
    def isAlive(self, tagID):
        print ("--- wifi isAlive")
        if self._sendRequest("isAlive?badgeUID=" + tagID) == "yes":
            return True
        else:
            return False

    def completeMinigame(self, tagID):
        print ("--- wifi completeMinigame")
        return self._sendRequest("minigameComplete?badgeUID=" + tagID)


    def startVoting(self):
        print ("--- wifi startVoting")
        self._sendRequest("startVote")
    
    def startEmergency(self):
        #Add screen output
        if self._sendRequest("checkVoteLimit"):
            if self._sendRequest("checkVoteCooldown"):#if cooldown is over
                voteType='meeting'
                self._sendRequest("useMeeting")
                self._sendRequest("setVoteType?type=" + voteType)#so the server knows a vote has started from emergency meeting
                self._sendRequest("startVote")
            else:
                return 'on cooldown'
    
    def startReportBody(self):
        print ("--- wifi startReportbody")
        #Add screen output
        voteType='report'
        self._sendRequest("setVoteType?type=" + voteType)#so the server knows a vote has started from dead body reported
        self._sendRequest("startVote")

    def requestStation(self, tagID):
        print ("--- wifi requeststation")
        return self._sendRequest("requestStation?badgeUID=" + tagID)

    def createSabotage(self, type):
        print ("--- wifi createsabotage")
        return self._sendRequest("sabotage?sabotageType=" + type)

    def completeSabotage(self,badgeUID):
        print ("--- wifi completeSabotage")
        return self._sendRequest("sabotageCompleted?badgeUID=" + badgeUID)

    def registerUser(self, tagID):
        print ("--- wifi registerUser")
        return self._sendRequest("registerUser?badgeUID=" + tagID)

    def startGame(self):
        print ("--- wifi startGame")
        return self._sendRequest('StartGame')

    def voteTally(self, badgeUID, myUID):
        print ("--- wifi voteTally")
        return self._sendRequest("voteTally?badgeUID="+badgeUID+"&myUID="+myUID)

    def initiateVote(self):
        print ("--- wifi initiateVote")
        return self._sendRequest("initiateVote")

    def voteTimeEnd(self):
        print ("--- wifi voteTimeEnd")
        return self._sendRequest("voteTimeEnd")

    def keepAlive(self):
        print ("--- wifi keepAlive")
        return self._sendRequest("keepAlive")

    def AutoDownloader(self):
        print ("--- wifi AutoDownloader")
        return self._sendRequest("AutoDownloader/GetFileList")

    def getTagName(self, uid):
        print ("--- wifi getTagName")
        return self._sendRequest("getTagName?uid=" + uid)

    def killPlayer(self, myUID, victimUID):
        print ("--- wifi killPlayer")
        return self._sendRequest("killPlayer?myUID={}&victimUID={}".format(myUID, victimUID))

    def isImposter(self, uid):
        print ("--- wifi isImposter")
        return self._sendRequest("isImposter?uid="+uid)

    def getFileList(self):
        print ("--- wifi getFileList")
        return self._sendRequest("AutoDownloader/GetFileList")

    def getFile(self, filename):
        print ("--- wifi getFile")
        return self._sendRequest("AutoDownloader/GetFile?fileName="+filename)

    def getPlayers(self):
        print ("--- wifi getPlayers")
        return json.loads(self._sendRequest("getPlayers"))
    
