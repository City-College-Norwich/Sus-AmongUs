from Minigame import Minigame
from IdleGame import IdleGame
from TimerHelper import *
from Screen import Screen
from Rfid import Rfid

class Download_Game:
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.progress = 0
        self.progress_width = 0
        self.download = False
        self.timer = TimerHelper()
        self.timer.Set(1000)
        pass
    
    def update(self):
        self.rfid = Rfid.do_read()
        if self.rfid:
            if self.timer.Check():
                self.progress_width = self.progress_width + self.progress
                progress_bar = self.display.fillRect(10, 10, self.progress_width, 30)
                self.progress = self.progress + 10
                Screen.display_text(progress_bar, 10, 10)
                Screen.draw_screen()

                if self.progress == 100:
                    self.parent.wifi.send_request(self, "minigameComplete?scannerId="+scannerId)
                    self.parent.currentMiniGame = IdleGame()
                    self.download = True
        else:
            Screen.display_text("Error: Walked away from task", 0, 0)
            Screen.draw_screen()

            