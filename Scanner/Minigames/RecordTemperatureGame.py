import random
from TimerHelper import *

from Minigames.Minigame import Minigame


class RecordTemperatureGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.current_temperature = random.randint(15, 33)
        self.logged_temperature = random.choice(random.choice(range(int(round(self.current_temperature/2)), self.current_temperature-5)), random.choice(range(self.current_temperature+5, self.current_temperature*2)))

        self.time = TimerHelper()
        self.time.set(500)

    def update(self):
        self.parent.screen.drawText("Record Temperature Game", 0, 0)
        self.parent.screen.drawText("Log Temperature", 0, 00)
        self.parent.screen.drawText("Current: " + str(self.current_temperature), 0, 10)
        self.parent.screen.drawText("Logged: " + str(self.logged_temperature), 0, 20)
        if self.logged_temperature == self.current_temperature:
            self.parent.wifi.sendRequest("minigameComplete?badgeUID=" + self.parent.badgeUID)
            self.parent.gotoGoodGuyGame()
        else:
            if self.time.check():
                buttons = self.parent.buttons.getPressedButtons()
                if buttons[0] == 1:
                    self.logged_temperature += 1
                elif buttons[2] == 1:
                    self.logged_temperature -= 1
                self.time.set(500)
