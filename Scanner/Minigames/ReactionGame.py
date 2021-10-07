import random
import time

from GoodGuyGame import GoodGuyGame
from Minigame import Minigame


class ReactionGame(Minigame):
    def __init__(self, parent):
        super().__init__(self, parent)
        self.parent = parent
        self.can_press_button = False
        time_to_change = random.randint(5, 16)
        self.endpoint = (time.ticks_ms() / 1000)+time_to_change
        self.state = False

    def update(self):
        if time.ticks_ms() / 1000 >= self.endpoint:

            self.state = not self.state
            self.parent.screen.fill(self.state)
            self.can_press_button = self.state

            if self.state:
                time_to_change = 2
                self.endpoint = (time.ticks_ms() / 1000)+time_to_change
            else:
                time_to_change = random.randint(5, 16)
                self.endpoint = (time.ticks_ms() / 1000)+time_to_change

        if self.can_press_button:
            buttons = self.parent.buttons.getPressedButtons()
            if buttons[0] == 1:
                self.parent.wifi.sendRequest(self, "minigameComplete?scannerId=" + self.parent.id)
                self.parent.currentMiniGame = GoodGuyGame()
