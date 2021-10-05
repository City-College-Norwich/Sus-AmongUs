""" Among Us Clone Scanner App
"""
import Buttons
import Rfid
import Screen
import Wifi
from Minigames.StartupGame import StartupGame


class App:
    def __init__(self):
        self.rfid = Rfid.Rfid(self)
        self.wifi = Wifi.Wifi()
        self.screen = Screen.Screen()
        self.buttons = Buttons.Buttons()

        self.currentMiniGame = StartupGame(self)

        self.id = 1
        self.isRunning = True

    def run(self):
        # mainloop
        while self.isRunning:
            # update modules
            self.currentMiniGame.update()
            # Send keepAlive to the server for updates
            self.keepAlive()

            # draw screen
            self.screen.draw_screen()

    def keepAlive(self):
        # if set amount of time has passed then
        # reset time
        # send msg to server
        # inform current minigame of results
        pass
