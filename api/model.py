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

                      # card ID,   team,   alive/dead
        self.players ={99:['team', True],}

        self.crewmateCount = 0
        self.imposterCount = 0

        self.maxImposters = 2

        self.sabotaged = False
        self.sabotage_time = 0
        self.sabotage_type = 0
        self.time = TimerHelper()

    def getTagName(self, uid):
        if uid in self.uids.keys():            
            return self.uids[uid] 
        else:
            return "No tags found"
            

    def startGame(self):
        i = 0
        while i < len(self.players):
            keys = list(self.players.keys())

            if self.imposterCount != self.maxImposters:
                randomPlayerIndex = random.randint(0, len(self.players) - 1)
                chosenPlayerUID = keys[randomPlayerIndex]
                if self.players[chosenPlayerUID][0] != "Imposter":
                    self.players[chosenPlayerUID][0] = "Imposter"
                    self.imposterCount += 1
                else:
                    print(str(chosenPlayerUID) + " is already a imposter, Itterating again!")
                    continue
            else:
                self.players[keys[i]][0] = "Crewmate"
                self.crewmateCount += 1
            i += 1
        
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


    def deadbodyfound(self, badgeUID):
        # split the playerId into the cmd (on the left) and the actual playerId# (on the right)

        if self.players[badgeUID][1] == False:
            startVote() #This needs creating first

    def registerUser(self,badgeUID):
        if badgeUID in self.players.keys(): 
            return "User is already Registered!"
            
        self.players[badgeUID] = ["team", True]
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

    def isAlive(self, badgeUID):
        if self.players[badgeUID][1]:
            return "yes"
        return "no"

    fileList = [
        "App.py", 
        "Buttons.py", 
        "Rfid.py", 
        "Screen.py", 
        "TimerHelper.py", 
        "Wifi.py",
        "Mingames/DownloadGame.py",
        "Minigames/GoodGuyGame.py",
        "Minigames/IdBadge.py",
        "Minigames/ImposterGame.py",
        "Minigames/Minigame.py",
        "Minigames/ReactionGame.py",
        "Minigames/RecordTemperatureGame.py",
        "Minigames/Sabotage1.py",
        "Minigames/StartupGame.py",
        "Minigames/UploadGame.py"]

    def getFileList(self):
        return json.dumps(self.fileList)

    def getFile(self, fileName):
        currentdir = os.path.dirname(os.path.realpath(__file__))
        parentdir = os.path.dirname(currentdir)

        if fileName in self.fileList:
            with open(os.join(parentdir, "/Scanner", fileName), "r") as f:
                file = f.read()
            return file
        return ""