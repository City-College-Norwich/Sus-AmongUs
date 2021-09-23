
from Minigame import Minigame
import random

'''
 game imports here                            
 from {file} import {class}                   
 e.g. from WiresMinigame import WiresMinigame 
'''
from IdBadge import IdBadge
from Reaction_Game import Reaction_Game


class IdleGame(Minigame):

    def __init__(self, parent):
        Minigame(self, parent)
        self.parent = parent

        # update bellow tuple with minigames
        self.__minigames = (IdBadge, Reaction_Game)

    def update(self):
        tag = self.parent.rfid.do_read()

        if tag == "miniGame":
            self.parent.currentMiniGame = random.choice(self.__minigames.__init__())


    def alertFromServer(self, alert):
        pass
