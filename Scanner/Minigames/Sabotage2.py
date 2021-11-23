import random

from Minigame import Minigame
from model import model
from GoodGuyGame import GoodGuyGame.minigames


class Sabotage2(Minigame):

    def __init__(self, parent):
        self.parent = parent
        self.__target_player = random.choice(self.parent.wifi.getPlayers())
        #chooses a random player tag to be used for sabotage.

    def update(self):
        if self.parent.badgeUID == self.__target_player:
            self.parent.screen.drawText("Your tasks Have been reset (＾ｖ＾) LOL", 0, 0)
            for x in self.parent.user_minigames_dict:
                self.parent.user_minigames_dict[x] = False
                #Sets their tasks back to false, can only ne used once.


