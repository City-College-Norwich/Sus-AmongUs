import random
import csv
from TimeHelper import TimeHelper

class Model:
    def __init__(self):

        with open('RFIDMap.csv', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            self.uids = {row[0]: row[1] for row in reader}

        self.totalMinigames = 10
        self.completedMinigames = 0


        self.GAME_STARTING = "Game_Starting"
        self.GAME_RUNNING = "Game_Running"
        self.GAME_ENDED = "Game_Ended"
        self.state = self.GAME_STARTING

                           # card ID,   team,   alive/dead
        self.players ={99:['player_uid', 'team', True],}
        self.crewmate = 0
        self.imposter = 0

        self.totalImposters = 2
        self.userID = 0
        self.sabotaged = False
        self.sabotage_time = 0
        self.sabotage_type = 0
        self.time = TimeHelper()

    def getTagName(self, uid):
        
        if uid in self.uids.keys():            
            return self.uids[uid] 
        else:
            return "No tags found"
            

    def startGame(self):
        self.state = self.GAME_RUNNING
        for i in range(0, len(self.players)):
            teamAssigner = random.randint(0,2)
            if self.crewmate == len(self.players) - self.totalImposters:
                teamAssigner = 1

            if self.imposter == self.totalImposters:
                teamAssigner = 0

            if teamAssigner == 0 :
                self.players[i][1] = "Crewmate"
                self.crewmate +=1
            elif teamAssigner == 1:
                self.players[i][1] = "Imposter"
                self.imposter += 1
        return self.state

      
    def callHomepage(self):
        return "hello"

    def requestStation(self):
        return "station" + str(random.choice(range(1, 11)))

    def minigameComplete(self, scannerId):
        self.completedMinigames += 1

    def keepAlive(self):
        alerts = set()
        
        if self.sabotaged == True:
            alerts.add("Sabotaged")
            return self.sabotage_type

        if self.totalImposters == 0:
            self.state = self.GAME_ENDED

        if self.completedMinigames >= self.totalMinigames:
            self.state = self.GAME_ENDED
        
        if self.state == self.GAME_ENDED:
            alerts.add("Game_Ended")

        return alerts

    def deadbodyfound(self, playerId):
        # split the playerId into the cmd (on the left) and the actual playerId# (on the right)
        result = playerId.split(':')
        id = result[1]
        
        if self.players [id][2] == False:
            startVote() #This needs creating first

    def askForID(self):
        self.userID += 1
        return self.userID

    def registerUser(self, scannerId, uid):
        self.players[scannerId] = [uid, "team", True]
        return "Okay"

    def sabotage(self, sabotageType):
        self.sabotaged = True
        self.sabotage_type = sabotageType


