import random

from Minigame import Minigame

'''
 game imports here                            
 from {file} import {class}                   
 e.g. from WiresMinigame import WiresMinigame 
'''
from IdBadge import IdBadge
from ReactionGame import ReactionGame


class IdleGame(Minigame):

    def __init__(self, parent):
        Minigame(self, parent)
        self.parent = parent

        # update bellow set with minigames
        self.__minigames = {IdBadge, ReactionGame}
        self.__target_station = self.parent.wifi.sendRequest("requestStation")

    def update(self):
        targetRfidTag = self.parent.rfid.do_read()

        if targetRfidTag == self.__target_station:
            self.parent.currentMiniGame = random.choice(self.__minigames.__init__())
        else:
            self.parent.screen.clear_screen()
            self.parent.screen.display_text(f"GOTO:{' ':<3}{self.__target_station:>8}")

    def alertFromServer(self, alert):
        pass
