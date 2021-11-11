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
        if tag == self.parent.badgeUID:
            self.parent.screen.drawText('Card Scanned', 0, 0)
            self.parent.wifi.sendRequest('minigameComplete?badgeUID=' + self.parent.badgeUID)
            self.parent.GoodGuyGame()
