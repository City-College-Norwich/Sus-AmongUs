
from Minigame import Minigame
import random

'''
 game imports here                            
 from {file} import {class}                   
 e.g. from WiresMinigame import WiresMinigame 
'''
from idBadge import ID_Badge

class IdleGame(Minigame):

    def __init__(self, parent):
        Minigame(self, parent)
        self.parent = parent

        ## update bellow tuple with minigames
        self.__minigames = (ID_Badge(), )

    def update(self):
        tag = self.parent.rfid.do_read()

        if tag == ".game":
            self.parent.currentMiniGame =  random.choice(self.__minigames)
            
        
    def alertFromServer(self, alert):
        pass
