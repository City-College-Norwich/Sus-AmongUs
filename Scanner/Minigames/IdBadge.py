from Minigames.Minigame import Minigame


class IdBadge(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.parent = parent

    def update(self):
        uid, tag = self.parent.rfid.doRead(True)
        self.parent.screen.drawText("Id Badge Game", 0, 0)
        self.parent.screen.drawText('Scan Card', 0, 20)
        self.check_card(uid)

    def check_card(self, uid):
        if uid == self.parent.badgeUID:
            self.parent.screen.drawText('-Card Scanned-', 0, 30)
            self.parent.wifi.completeMinigame(self.parent.badgeUID)
            self.parent.isMinigameCompleted = True #So GoodGuyGame knows a minigame was completed
            self.parent.lastMinigame = IdBadge #So GoodGuyGame knows what minigame was completed
            self.parent.gotoIdleGame()