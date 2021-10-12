""" Among Us Clone Scanner App
"""
import json

from dotenv import load_dotenv
load_dotenv()
import os
mode = os.environ.get("MODE")
print("System Mode: " + mode)

import Buttons
import Rfid
import Screen
import Wifi
from TimerHelper import TimerHelper
from Minigames.StartupGame import StartupGame
from Minigames.Minigame import Minigame
from Minigames.GoodGuyGame import GoodGuyGame
from Minigame.IdBadge import IdBadge
from Minigame.ReactionGame import ReactionGame
from Minigame.Sabotage1 import Sabotage1

KEEP_ALIVE_TIMEOUT = 500  # timeout in ms


class App:
    def __init__(self):
        self.rfid = Rfid.Rfid(self)
        self.wifi = Wifi.Wifi()
        self.screen = Screen.Screen()
        self.buttons = Buttons.Buttons()

        self.currentMiniGame = StartupGame(self)

        self.id = 1
        self.isRunning = True
        self.keep_alive_timer = TimerHelper()

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

            alerts = set(json.loads(self.wifi.sendRequest("keepAlive")))

            self.currentMiniGame.alertsFromServer(alerts)
            self.keep_alive_timer.set(KEEP_ALIVE_TIMEOUT)
