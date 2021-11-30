from Minigames.Minigame import Minigame
from TimerHelper import *
class VotingGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)

        self.alive = self.parent.wifi.isAlive(self.parent.badgeUID)
        self.parent.screen.clear()
        if self.alive:
            if self.parent.votingType == 'meeting':
                self.parent.screen.drawText("EmergencyMeeting", 0, 0)
            elif self.parent.votingType == 'report':
                self.parent.screen.drawText("Body Reported", 0, 0)
            self.parent.screen.drawText("Go to vote room ", 0, 20)
            self.parent.screen.drawText("      and", 0, 30)
            self.parent.screen.drawText(" Scan vote tag ", 0, 40)
        else:
            self.parent.screen.drawText("You are dead", 0, 0)
            self.parent.screen.drawText("Go to vote room", 0, 20)
            self.parent.screen.drawText("Tell everyone", 0, 40)
            self.parent.screen.drawText("you are dead", 0, 50)

        self.voted = False
        self.InitiateVoting = False


    def update(self):
        if self.alive:
            uid,tag = self.parent.rfid.doRead(True)

            if self.InitiateVoting == False:
                if tag == ".votingHub":
                    self.parent.wifi.joinVote(self.parent.badgeUID)
                    self.parent.screen.clear()                
                    self.parent.screen.drawText("   -Voting-", 0, 0)
                    self.parent.screen.drawText("Wait for Vote", 0, 20)
                    self.parent.screen.drawText("to Start", 0, 30)
            else:
    
                if self.voted==False:
                    self.parent.screen.clear()
                    self.parent.screen.drawText("   -Voting-", 0, 0)
                    self.parent.screen.drawText("Scan player tag ", 0, 20)
                    self.parent.screen.drawText("    to vote ", 0, 30)
                if tag is not None and tag[:8] == 'playerId' and self.voted == False:
                    if self.parent.wifi.isAlive(self.parent.badgeUID):
                        self.parent.wifi.voteTally(uid, self.parent.badgeUID)
                    self.parent.screen.clear()
                    self.parent.screen.drawText("   -Voting-", 0, 0)
                    self.parent.screen.drawText(" You have voted. ", 0, 20)
                    self.voted = True


    def alertsFromServer(self, alerts):
        Minigame.alertsFromServer(self, alerts)
        if "Start_Voting" not in alerts:
            self.parent.gotoIdleGame()
        elif "Initiate_Voting" in alerts:
            self.InitiateVoting = True
