import random

class Team_Select:
    def __init__(self):
        self.Crewmate = 0
        self.Imposter = 0
        pass

    def assign_team(self, players):
        for i in range(0, len(players)):
            team_assigner = random.randint(0,2)
            if self.Crewmate == 8:
                team_assigner == 1

            if self.Imposter == 2:
                team_assigner == 0

            if team_assigner == 0 :
                players[i][1] = "Crewmate"
                self.Crewmate +=1
            elif team_assigner == 1:
                players[i][1] = "Imposter"
                self.Imposter += 1