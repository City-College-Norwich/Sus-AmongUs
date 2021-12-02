import random

from Minigame import Minigame
from Scanner.TimerHelper import TimerHelper


class Sabotage2(Minigame):

    def __init__(self, parent, sabotagedPlayerUID):
        Minigame.__init__(self, parent)
        self.parent = parent
        self.__delay_timer = TimerHelper()
        self.__delay_timer.set(10000)

        self.parent.screen.drawText("SABOTAGE!", 0, 0)

        if self.parent.badgeUID == sabotagedPlayerUID:
            for x in self.parent.user_minigames_dict:
                self.parent.user_minigames_dict[x] = False
                # Sets their tasks back to false, can only be used once.
            self.parent.screen.drawText("Your tasks have", 0, 20)
            self.parent.screen.drawText("been reset", 0, 30)
            self.parent.screen.drawText("(＾ｖ＾) LOL", 0, 40)
        else:
            self.parent.screen.drawText("The Imposters", 0, 20)
            self.parent.screen.drawText("have sabotaged", 0, 30)
            self.parent.screen.drawText("someones tasks!!", 0, 40)

    def update(self):
        if self.__delay_timer.check():
            self.parent.gotoIdleGame()
        

