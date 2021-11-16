from Minigames.Minigame import Minigame


class IdBadge(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.parent = parent

        self.parent.screen.drawText('Scan Card', 0, 0)

    def update(self):
        tag = self.parent.rfid.doRead()
        self.parent.screen.drawText("Id Badge Game", 0, 0)

        self.check_card(tag)

    def check_card(self, tag):
        if tag == 'card':  # TODO- get format of id card data.
            self.parent.screen.drawText('Card Scanned', 0, 0)
            self.parent.wifi.completeMinigame(self.parent.badgeUID)
            self.parent.isMinigameCompleted = True #So GoodGuyGame knows a minigame was completed
            self.parent.lastMinigame = IdBadge #So GoodGuyGame knows what minigame was completed
            self.parent.gotoGoodGuyGame()