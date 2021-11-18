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
from Minigames.Sabotage3 import Sabotage3
from Minigames.ImposterGame import ImposterGame

from Minigames.VotingGame import VotingGame


KEEP_ALIVE_TIMEOUT = 500  # timeout in ms


class App:
    STARTING = 0
    RUNNING = 1
    VOTING = 2
    CREWMATE_WIN = 3
    IMPOSTOR_WIN = 4



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
        team = self.wifi.isImposter(self.badgeUID)
        team = "False" if team is None else team
        if team == "False":
            self.currentMiniGame = GoodGuyGame(self)
        else:
            self.currentMiniGame = ImposterGame(self)

    def gotoSabotageGame1(self,sabotagedStation):
        self.currentMiniGame = Sabotage1(self,sabotagedStation)

    def gotoSabotageGame3(self,sabotagedStation):
        self.currentMiniGame = Sabotage3(self,sabotagedStation)
    
    def gotoVotingGame(self):
        self.state = self.VOTING
        self.currentMiniGame = VotingGame(self)


