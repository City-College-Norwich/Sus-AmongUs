import random
import csv
import json

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
        self.players ={99:['player_uid', 'team', True],}

        self.crewmateCount = 0
        self.imposterCount = 0


        self.maxImposters = 2

        self.userID = 0
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
        self.state = GAME_RUNNING

        i = 0
        while i != len(self.players) - 1:
            keys = list(self.players.keys())

            if self.imposterCount != self.maxImposters:
                randomPlayerIndex = random.randint(0, len(self.players) - 1)
                chosenPlayerUID = keys[randomPlayerIndex]
                if self.players[chosenPlayerUID][1] != "Imposter":
                    self.players[chosenPlayerUID][1] = "Imposter"
                    self.imposterCount += 1
                    i += 1
                else:
                    print(chosenPlayerUID + " is already a imposter, Itterating again!")
            else:
                self.players[keys[i]][1] = "Crewmate"
                self.crewmateCount += 1
        return "okay"

      
    def callHomepage(self):
        return "hello"

    def requestStation(self):
        return "station" + str(random.choice(range(1, 6)))

    def minigameComplete(self, scannerId):
        self.completedMinigames += 1

    def keepAlive(self):
        alerts = set()
        if self.state == GAME_RUNNING:
            alerts.add("GameStarted")
            if self.sabotaged:
                alerts.add("Sabotaged")

            if self.imposterCount == 0:
                self.state = CREWMATE_WIN
                alerts.add("Crewmates_Win")
            elif self.crewmateCount == 0:
                self.state = IMPOSTER_WIN
                alerts.add("Imposter_Win")

        return json.dumps(list(alerts))


    def deadbodyfound(self, playerId):
        # split the playerId into the cmd (on the left) and the actual playerId# (on the right)
        result = playerId.split(':')
        id = result[1]
        
        if self.players [id][2] == False:
            startVote() #This needs creating first

    def askForID(self):
        self.userID += 1
        return str(self.userID)

    def registerUser(self, scannerId, uid):
        if scannerId in self.players.keys(): 
            return "User is already Registered!"
            
        self.players[scannerId] = [uid, "team", True]
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
