import random

from Minigames.Minigame import Minigame


class RecordTemperatureGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.current_temperature = random.randint(15, 33)
        self.temperature_upper_bound = self.current_temperature * 2
        self.temperature_lower_bound = self.current_temperature+5
        self.logged_temperature = random.randint(self.temperature.lower_bound, self.temperature.upper_bound)

    def update(self):
        self.parent.screen.drawText("Current Temperature: " + self.current_temperature, 0, 0)
        self.parent.screen.drawText("Logged Temperature: " + self.logged_temperature, 0, 20)
        if self.logged_temperature == self.current_temperature:
            self.parent.wifi.sendRequest(self, "minigameComplete?scannerId=" + self.parent.id)
            self.parent.currentMiniGame = GoodGuyGame()
        else:
            buttons = self.parent.buttons.getPressedButtons()
            if buttons[0] == 1:
                self.logged_temperature += 1
            elif buttons[2] == 1:
                self.logged_temperature -= 1
