import random
import csv
import json
import os, sys

from TimerHelper import TimerHelper

GAME_STARTING = 1
GAME_RUNNING = 2
GAME_ENDED = 3
CREWMATE_WIN = 4
IMPOSTER_WIN = 5

class Model:
    def __init__(self):

        with open('RFIDMap.csv', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            self.uids = {row[0]: row[1] for row in reader}

        self.totalMinigames = 10
        self.completedMinigames = 0
        self.state = GAME_STARTING

                      # card ID,   team,   alive/dead, votecounter, voted
        self.players ={"0x14742558":['crewmate', False, 0, 0]}

        self.crewmateCount = 0
        self.imposterCount = 0

        self.maxImposters = 1

        self.sabotaged = False
        self.sabotage_time = 0
        self.sabotage_type = 0
        self.time = TimerHelper()
        self.playerTotalVote = 0
        self.totalVote = 0
        self.voting = False

    def getTagName(self, uid):
        if uid in self.uids.keys():            
            return self.uids[uid] 
        else:
            return "No tags found"
            
    def startGame(self):
        players = list(range(len(self.players.keys())))
        for i in range(self.maxImposters):
            imposter = players.pop(random.randint(0, len(players)-1))
            self.players[self.players.keys()[imposter]][0] = "Imposter"
            self.imposterCount += 1
        
        for crewmate in players:
            self.players[self.players.keys()[crewmate]][0] = "Crewmate"
        self.crewmateCount = len(players)
        
        self.state = GAME_RUNNING
        return "okay"
      
    def callHomepage(self):
        return "hello"

    def requestStation(self):
        return "station" + str(random.choice(range(1, 6)))

    def minigameComplete(self, scannerId):
        self.completedMinigames += 1
        return "Okay"

    def keepAlive(self):
        alerts = set()
        if self.state == GAME_RUNNING:
            alerts.add("GameStarted")
            if self.sabotaged:
                alerts.add("Sabotaged")
            elif self.voting == True:
                alerts.add("Voting")

            if self.imposterCount == 0:
                self.state = CREWMATE_WIN
                alerts.add("Crewmates_Win")
            elif self.crewmateCount == self.imposterCount:
                self.state = IMPOSTER_WIN
                alerts.add("Imposter_Win")

        return json.dumps(list(alerts))

    def killPlayer(self, badgeUID):
        self.players[badgeUID][1] = False
        if self.players[badgeUID][0] == "Imposter":
            self.imposterCount -= 1
        else:
            self.crewmateCount -= 1
        return "ok"

    def startVote(self):
        self.totalVote = 0
        i = 0
        while i < len(self.players):
            keys = self.players.keys()
            self.players[keys[i]][2] = 0
            self.players[keys[i]][3] = 0
            i+=1
        self.voting = True
        return "ok"
        
    def registerUser(self,badgeUID):
        if badgeUID in self.players.keys(): 
            return "User is already Registered!"
            
        self.players[badgeUID] = ["team", True, 0, 0]
        self.uids[badgeUID] = "playerId"
        return "Okay"

    def sabotage(self, sabotageType):
        self.sabotaged = True
        self.sabotage_type = sabotageType

    def getSabotageType(self):
        return self.sabotage_type

    def sabotageTimeout(self):
        self.state = IMPOSTER_WIN

    def sabotageCompleted(self):
        self.sabotaged = False

    def voteTally(self, badgeUID, myUID):
        self.playerTotalVote = int(self.players[badgeUID][2]) + 1
        self.players[badgeUID][2] = str(self.playerTotalVote)
        self.players[myUID][3] = 1
        self.totalVote += 1
        return "ok"
        
    def isAlive(self, badgeUID):
        if self.players[badgeUID][1]:
            return "yes"
        return "no"

    
    def isImposter(self, uid):
        if self.players[uid][0] == "Imposter":
            return "True"
        return "False"
       


    fileList = [
        "App.py", 
        "Buttons.py", 
        "Rfid.py", 
        "Screen.py", 
        "TimerHelper.py", 
        "Wifi.py",
        "boot.py",
        "Minigames/DownloadGame.py",
        "Minigames/GoodGuyGame.py",
        "Minigames/IdBadge.py",
        "Minigames/ImposterGame.py",
        "Minigames/Minigame.py",
        "Minigames/ReactionGame.py",
        "Minigames/RecordTemperatureGame.py",
        "Minigames/Sabotage1.py",
        "Minigames/StartupGame.py",
        "Minigames/UploadGame.py",
        "Minigames/VotingGame.py"]

    def getFileList(self):
        return json.dumps(self.fileList)

    def getFile(self, fileName):
        currentdir = os.path.dirname(os.path.realpath(__file__))
        parentdir = os.path.dirname(currentdir)
        scannerdir = os.path.join(parentdir, "Scanner")

        if fileName in self.fileList:
            with open(os.path.join(scannerdir, fileName), "r") as f:
                file = f.read()
            return file
        return ""
