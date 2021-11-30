from Minigames.Minigame import Minigame
from TimerHelper import *
class VotingGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)

        
        if self.parent.votingType == 'meeting':
            self.parent.screen.drawText("EmergencyMeeting", 0, 0)
        elif self.parent.votingType == 'report':
            self.parent.screen.drawText("Body Reported", 0, 0)
        self.parent.screen.drawText("Go to vote room ", 0, 20)
        self.parent.screen.drawText("      and", 0, 30)
        self.parent.screen.drawText(" Scan vote tag ", 0, 40)


        self.voted = False
        self.InitiateVoting = False


    def update(self):
        uid,tag = self.parent.rfid.doRead(True)
        self.rfid = self.parent.rfid.doRead()
        self.parent.TotalVoters += 1
        if self.InitiateVoting == False:
            if tag == ".votingHub":
                self.parent.wifi.joinVote(self.parent.badgeUID)
        else:
 
            if self.voted==False:
                self.parent.screen.clear()
                self.parent.screen.drawText("   -Voting-", 0, 0)
                self.parent.screen.drawText("Scan player tag ", 0, 20)
                self.parent.screen.drawText("    to vote ", 0, 30)
            if tag is not None and tag[:8] == 'playerId' and self.voted == False:
                if self.parent.wifi.isAlive(self.parent.badgeUID):
                    self.parent.screen.clear()
                    self.player2kill = self.parent.wifi.voteTally(uid, self.parent.badgeUID)
                    if self.player2kill != "ok" and self.player2kill != "draw":
                        self.parent.executePlayer(self.player2kill[0])
                        self.parent.screen.drawText(self.player2kill[1][4] + " Ejected", 0, 0)
                        self.parent.screen.drawText(self.player2kill[1][4], 0, 10)
                        self.parent.screen.drawText("was a " + self.player2kill[1][0], 0, 20)

                elif self.player2kill == "draw":
                    self.parent.screen.drawText("No one Ejected", 0, 0)
                self.parent.screen.drawText("   -Voting-", 0, 0)
                self.parent.screen.drawText(" You have voted. ", 0, 20)
                self.voted = True

    def alertsFromServer(self, alerts):
        Minigame.alertsFromServer(self, alerts)
        if "Start_Voting" not in alerts:
            self.parent.gotoIdleGame()
        elif "Initiate_Voting" in alerts:
            self.InitiateVoting = True
