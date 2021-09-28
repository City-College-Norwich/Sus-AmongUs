from Minigame import Minigame
from IdleGame import IdleGame
from TimerHelper import *

class Upload_Game:
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.progress = 0
        self.progress_width = 0
        self.timer = TimerHelper()
        self.timer.Set(1000)
        pass
    
    def update(self):
        self.rfid = self.parent.rfid.do_read()
        if self.rfid:
            if self.timer.Check():
                self.progress_width = self.progress_width + self.progress
                self.progress = self.progress + 10
                self.parent.screen.display_rectangle(10, 10, self.progress_width, 30)
                self.timer.Set(1000)

                if self.progress > 100:
                    self.parent.wifi.send_request(self, "minigameComplete?scannerId="+self.parent.id)
                    self.parent.currentMiniGame = IdleGame()
                    
            else:
                self.parent.screen.display_text("Error: Download Task not complete", 0, 0)
        else:
            self.parent.screen.display_text("Error: Walked away from task", 0, 0)