from Minigames.Minigame import Minigame

class VotingGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.parent.screen.drawText("Voting Started", 0, 0)
        self.parent.screen.drawText("Go to Voting Room ", 0, 20)
        self.parent.screen.drawText("Scan Players Badge ", 0, 40)

        self.voted = False

    def update(self):
        uid,tag = self.parent.rfid.doRead(True)
        if tag is not None and tag[:8] == 'playerId' and self.voted == False:
            if self.parent.wifi.sendRequest("isAlive?badgeUID=" + self.parent.badgeUID)=='yes':
                self.parent.wifi.sendRequest("voteTally?badgeUID="+uid)
            self.voted = True

    def alertsFromServer(self, alerts):
        Minigame.alertsFromServer(self, alerts)
        if alerts["Voting"] == False:
            self.parent.gotoIdleGame()