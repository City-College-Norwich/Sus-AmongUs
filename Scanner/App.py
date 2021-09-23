""" Among Us Clone Scanner App
"""
from StartupGame import Startupgame
import Rfid, Wifi, Screen, Buttons

class App:
    def __init__(self):
        self.rfid = Rfid.Rfid()
        self.wifi = Wifi.Wifi()
        self.screen = Screen.Screen()
        self.buttons = Buttons.Buttons()

        self.currentMiniGame = Startupgame(self)

        self.id = 1
        self.isRunning = True

        

    def run(self):
        # mainloop
        while self.isRunning:
            # update modules
            self.rfid.update()

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



        
        

            
