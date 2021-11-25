import random

from Minigame import Minigame
from Scanner.TimerHelper import TimerHelper


class Sabotage2(Minigame):

    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.parent = parent
        self.__target_player = random.choice(self.parent.wifi.getPlayers())
        self.__delay_timer = TimerHelper()
        self.__delay_timer.set(75000)
        # chooses a random player tag to be used for sabotage.
        if self.parent.badgeUID == self.__target_player:
            for x in self.parent.user_minigames_dict:
                self.parent.user_minigames_dict[x] = False
                # Sets their tasks back to false, can only be used once.

    def update(self):
        if self.__delay_timer.check():
            self.parent.gotoIdleGame()
        else:
            if self.parent.badgeUID == self.__target_player:
                self.parent.screen.drawText("Your tasks Have been reset (＾ｖ＾) LOL")
            else:
                self.parent.screen.drawText("The Imposters have sabotaged someones tasks!!")
