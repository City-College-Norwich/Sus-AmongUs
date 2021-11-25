from Minigames.Minigame import Minigame
from TimerHelper import TimerHelper


class Sabotage3(Minigame):
    def __init__(self, parent,sabotagedStation):
        print ("--- sabotage3")
        super().__init__(parent)
        self.parent = parent
        self.__target_station = sabotagedStation
        self.alreadyScanned = False

    def update(self):
        print ("--- sabotage3 update")
        if not self.alreadyScanned:
            self.parent.screen.clear()
            self.parent.screen.drawText("GOTO: " + self.__target_station, 0, 0)
            if self.parent.rfid.doRead() == self.__target_station:
                self.parent.wifi.completeSabotage(self.parent.badgeUID)
                self.alreadyScanned = True
    