from Minigames.Minigame import Minigame

class VotingGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.parent.screen.drawText("Voting Started", 0, 0)
        self.parent.screen.drawText("Go to Voting Room ", 0, 20)
        self.parent.screen.drawText("Scan Players Badge ", 0, 40)
        self.MyUID = self.parent.badgeUID

        self.voted = False

    def update(self):
        targetRfidTag = self.parent.rfid.doRead()
            # check if the first 7 characters == playerId
            # if yes, then split at the colon and get the playerId number (just like in model)
            # send that playerId in the sendRequest

            #targetRfidTag = 'playerId:12'
        if targetRfidTag is not None and targetRfidTag[:8] == 'playerId' and self.voted == False: #number of players weather they have voted 
            if self.parent.wifi.sendRequest("isAlive?badgeUID=" + self.parent.badgeUID)=='yes': #if they are alive then
                playerId = targetRfidTag.split(':')                                             #scan for vote
                self.parent.wifi.sendRequest("voteTally?badgeUID="+playerId[10]+"myUID="+self.MyUID)                 #tallys the vote
                self.voted = True                                                               # ends voting once all players who voted 
            elif self.parent.wifi.sendRequest("isAlive?badgeUID=" + self.parent.badgeUID)=='no':#if they are dead
                self.voted = True                                                               #they can't vote 

