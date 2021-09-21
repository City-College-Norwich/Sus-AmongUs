""" Among Us Clone Scanner App
"""
from StartupGame import Startupgame


class App:
    def __init__(self):
        self.rfid = Rfid()
        self.wifi = None
        self.screen = None
        self.buttons = None

        self.currentMiniGame = Startupgame(self)

        self.id = 1
        self.isRunning = True

        

    def run(self):
        # mainloop
        while self.isRunning:
            # update modules
            

            # Send keepAlive to the server for updates
            self.keepAlive()    

            # draw screen


            pass


    def keepAlive(self):
        # if set amount of time has passed then
            # reset time
            # send msg to server
            # inform current minigame of results
        pass



        
        

            
