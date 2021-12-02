""" Among Us Clone Scanner App
"""
import json

# from dotenv import load_dotenv
# load_dotenv()
# import os
# mode = os.environ.get("MODE")
# print("System Mode: " + mode)

import Buttons
import Rfid
import Screen
import Wifi
from TimerHelper import TimerHelper
from Minigames.StartupGame import StartupGame
from Minigames.GoodGuyGame import GoodGuyGame
from Minigames.Sabotage1 import Sabotage1
from Minigames.Sabotage2 import Sabotage2
from Minigames.Sabotage3 import Sabotage3
from Minigames.ImposterGame import ImposterGame

from Minigames.VotingGame import VotingGame

from Minigames.DownloadGame import DownloadGame
from Minigames.IdBadge import IdBadge
from Minigames.ReactionGame import ReactionGame
from Minigames.RecordTemperatureGame import RecordTemperatureGame
from Minigames.UploadGame import UploadGame

KEEP_ALIVE_TIMEOUT = 500  # timeout in ms


class App:
    STARTING = 0
    RUNNING = 1
    VOTING = 2
    CREWMATE_WIN = 3
    IMPOSTOR_WIN = 4
    SABOTAGED = 5

    def __init__(self):
        self.rfid = Rfid.Rfid(self)
        self.screen = Screen.Screen()
        self.wifi = Wifi.Wifi(self)
        self.buttons = Buttons.Buttons()

        self.currentMiniGame = StartupGame(self)

        self.badgeUID = None
        self.isRunning = True
        self.keep_alive_timer = TimerHelper()
        self.state = self.STARTING
        self.isMinigameCompleted = False
        self.lastMinigame = None
        self.votingType=None

        self.user_minigames_dict = {
            DownloadGame: False,
            IdBadge: False,
            ReactionGame: False,
            RecordTemperatureGame: False,
            UploadGame: False,
        }

    def run(self):
        self.keep_alive_timer.set(KEEP_ALIVE_TIMEOUT)
        # mainloop
        while self.isRunning:
            # update modules
            self.currentMiniGame.update()
            # Send keepAlive to the server for updates
            self.keepAlive()

            # draw screen
            self.screen.draw()

    def keepAlive(self):
        if self.keep_alive_timer.check():
            alerts = json.loads(self.wifi.keepAlive())

            self.currentMiniGame.alertsFromServer(alerts)
            self.keep_alive_timer.set(KEEP_ALIVE_TIMEOUT)

    def gotoIdleGame(self):
        self.state = self.RUNNING
        team = self.wifi.isImposter(self.badgeUID)
        team = "False" if team is None else team
        if team == "False":
            self.currentMiniGame = GoodGuyGame(self)
        else:
            self.currentMiniGame = ImposterGame(self)

    def gotoSabotageGame(self, sabotageType, sabotageData):
        print ("dddddddd")
        print (self.wifi.isImposter(self.badgeUID))
    
        if self.wifi.isImposter(self.badgeUID) != "False":
            return
        print ("xxxxxxxxx")
        print (sabotageType)
        print (type(sabotageType))
        if sabotageType == 1:
            self.currentMiniGame = Sabotage1(self, sabotageData)
        elif sabotageType == 2:
            print ("sabotage type 2")
            self.currentMiniGame = Sabotage2(self, sabotageData)
            print (self.currentMiniGame)
        elif sabotageType == 3:
            self.currentMiniGame = Sabotage3(self, sabotageData)
        print (self.currentMiniGame)
        
    
    def gotoVotingGame(self,type):
        self.state = self.VOTING
        self.votingType=type
        self.currentMiniGame = VotingGame(self)
