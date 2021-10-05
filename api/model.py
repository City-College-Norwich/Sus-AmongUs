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
        self.Crewmate = 0
        self.Imposter = 0
        self.totalImposters = 2


    def getTagName(self, uid):
        return self.uids[uid] 

    def startGame(self):
        self.state = "Game_Running"
        for i in range(0, len(self.players)):
            team_assigner = random.randint(0,2)
            if self.Crewmate == len(self.players) - self.totalImposters:
                team_assigner = 1

            if self.Imposter == self.totalImposters:
                team_assigner = 0

            if team_assigner == 0 :
                self.players[i][1] = "Crewmate"
                self.Crewmate +=1
            elif team_assigner == 1:
                self.players[i][1] = "Imposter"
                self.Imposter += 1
        return self.state

      
    def callHomepage(self):
        return "hello"

    def requestStation(self):
        return "station" + str(random.choice(range(1, 11)))

    def minigameComplete(self, scannerId):
        self.completedMinigames += 1

    def keepAlive(self):
        alerts = set()

        if self.completedMinigames >= self.totalMinigames:
            self.state = "Game_Ended"
        
        if self.state == "Game_Ended":
            alerts.add("Game_Ended")

        return alerts
