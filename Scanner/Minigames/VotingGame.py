from Minigames.Minigame import Minigame
from TimerHelper import *

class VotingGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)

        self.parent.screen.clear()
        if self.parent.votingType == 'meeting':
            self.parent.screen.drawText("Emergency Meeting!", 0, 0)
        elif self.parent.votingType == 'report':
            self.parent.screen.drawText("Dead Body Reported!", 0, 0)
        self.parent.screen.drawText("Go to Voting Room ", 0, 20)
        
        '''#Old display text - Not sure if is still needed
        self.parent.screen.clear()
        self.parent.screen.drawText("Voting Started", 0, 0)

        self.parent.screen.drawText("Go to Voting", 0, 20)
        self.parent.screen.drawText("Room", 0, 30)
        self.parent.screen.drawText("Scan Vote tag ", 0, 50)
'''

        self.voted = False
        self.InitiateVoting = False

        self.timer = TimerHelper()
        self.timer.set(60000)

    def update(self):
        uid,tag = self.parent.rfid.doRead(True)
        if self.InitiateVoting == False:
            if tag == ".votingHub":
                self.parent.wifi.initiateVote()
        else:
            if self.timer.check():
                self.parent.wifi.voteTimeEnd()
                
            self.parent.screen.drawText("Voting", 0, 0)
            self.parent.screen.drawText("Scan Player tag ", 0, 20)
            if tag is not None and tag[:8] == 'playerId' and self.voted == False:
                if self.parent.wifi.isAlive(self.parent.badgeUID):
                    self.parent.wifi.voteTally(uid, self.parent.badgeUID)
                self.voted = True

    def alertsFromServer(self, alerts):
        Minigame.alertsFromServer(self, alerts)
        if "Start_Voting" not in alerts:
            self.parent.gotoIdleGame()
        elif "Initiate_Voting" in alerts:
            self.InitiateVoting = True
