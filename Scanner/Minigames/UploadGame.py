from Minigames.Minigame import Minigame
from TimerHelper import *
import random


class UploadGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.progress = 0
        self.progress_width = 0
        self.timer = TimerHelper()
        self.timer.set(1000)
        self.rfid = False
        pass

    def update(self):
        self.rfid = self.parent.rfid.doRead()
        self.parent.screen.clear()
        self.parent.screen.drawText("Upload Game", 0, 0)
        if self.rfid:
            if self.timer.check():
                self.progress_width += random.choice(range(5, 16))
                self.progress = self.progress_width
                self.parent.screen.drawText("Keep Scanning", 0, 10)
                self.parent.screen.drawRectangle(10, 20, self.progress_width, 25)
                self.parent.screen.drawText(str(self.progress) + "%", 50, 55)
                self.timer.set(1000)


                if self.progress >= 100:
                    self.parent.wifi.completeMinigame(self.parent.badgeUID)
                    self.parent.isMinigameCompleted = True
                    self.parent.lastMinigame = UploadGame

            else:
                self.parent.screen.clear()
                self.parent.screen.drawText("Error: Download Task not complete", 0, 0)
        else:
            self.parent.screen.clear()
            self.parent.screen.drawText("Keep Scanning", 0, 0)
            self.parent.screen.drawRectangle(10, 20, self.progress_width, 15)
            self.parent.screen.drawText(str(self.progress) + "%", 50, 45)
