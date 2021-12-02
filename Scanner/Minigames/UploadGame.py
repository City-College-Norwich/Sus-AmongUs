from Minigames.Minigame import Minigame
from TimerHelper import *
import random


class UploadGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self,parent)
        self.parent = parent
        self.progress = 0
        self.timer = TimerHelper()
        self.timer.set(1000)
        self.rfid = False


    def update(self):
        self.rfid = self.parent.rfid.doRead()

        if self.rfid:
            if self.timer.check():
                self.progress += random.choice(range(5, 16))
                if self.progress > 100:
                    self.progress = 100
                self.drawUI()
                self.timer.set(1000)
        else:
            self.drawUI()

        if self.progress >= 100:
            self.parent.wifi.completeMinigame(self.parent.badgeUID)
            self.parent.isMinigameCompleted = True
            self.parent.lastMinigame = UploadGame
            self.parent.gotoIdleGame()

    def drawUI(self):
        self.parent.screen.clear()
        self.parent.screen.drawText("Upload Game", 0, 0)
        self.parent.screen.drawText("Keep Scanning", 0, 10)
        self.parent.screen.drawRectangle(10, 20, self.progress, 25)
        self.parent.screen.drawText(str(self.progress) + "%", 50, 55)