from Team_Select import Team_Select
import random
import csv

class Model:
    def __init__(self):

        with open('RFIDMap.csv', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            self.uids = {row[0]: row[1] for row in reader}

        self.totalMinigames = 10
        self.completedMinigames = 0
        self.state = "Game_Starting"
        self.players ={99:['player_uid', 'team'],}

    def getTagName(self, uid):
        return self.uids[uid] 

    def startGame(self):
        self.state = "Game_Running"
        self.Team_Select.assign_team(self.players)
        return self.state

      
    def callHomepage(self):
        return "hello"

    def requestStation(self):
        return "station" + str(random.choice(range(1, 11)))

    def minigameComplete(self, scannerId):
        self.completedMinigames += 1

    def keepAlive(self):
        if self.completedMinigames >= self.totalMinigames:
            self.state = "Game_Ended"
        
        if self.state == "Game_Ended":
            return "Game_Ended"
