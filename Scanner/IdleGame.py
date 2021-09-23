
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
        self.__target_station = "stationAssignment"

    def update(self):
        tag = self.parent.rfid.do_read()

        if tag == self.__target_station and self.__target_station == "stationAssignment":

            if self.__target_station == "stationAssignment":
                self.__target_station = self.parent.wifi.send_request("requestStation")
                self.parent.screen.clear_screen()
                self.parent.screen.display_text("GOTO: " + self.__target_station)

            else:
                self.parent.currentMiniGame = random.choice(self.__minigames.__init__())

        else:
            self.parent.screen.clear_screen()
            self.parent.screen.display_text("GOTO: " + self.__target_station)


    def alertFromServer(self, alert):
        pass
