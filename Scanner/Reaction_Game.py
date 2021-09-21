from Minigame import Minigame
from IdleGame import IdleGame
import random
import time

class Reaction_Game:
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.parent = parent
        self.can_press_button = False
        time_to_change = Random.randint(5,16)
        self.endpoint = (time.ticks_ms()/1000) + time_to_change

        self.state = "Black"

    def update():
        if time.ticks_ms()/1000 >= self.endpoint:
            if self.state == "Black":
                self.parent.screen.fill(1)
                self.can_press_button = True
                self.state = "White"
                time_to_change = 2
                self.endpoint = (time.ticks_ms()/1000) + time_to_change
                
            elif self.state == "White":
                self.state = "Black"
                self.can_press_button = False
                self.parent.screen.fill(0)
                time_to_change = Random.randint(5,16)
                self.endpoint = (time.ticks_ms()/1000) + time_to_change

        
        if self.can_press_button == True:
            buttons = self.parent.buttons.getPressedButtons()
            if buttons[0] == 1:
                self.parent.wifi.send_request(self, "Reaction_Game Complete")
                self.parent.currentMiniGame = IdleGame()

