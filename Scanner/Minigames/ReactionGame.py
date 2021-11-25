import random

from Minigames.Minigame import Minigame
from TimerHelper import *


class ReactionGame(Minigame):
    def __init__(self, parent):
        print ("--- reactionGame")
        Minigame.__init__(self, parent)
        self.parent = parent
        self.can_press_button = False
        time_to_change = random.randint(5, 16)
        self.timer = TimerHelper()
        self.timer.set(time_to_change*1000)
        self.state = False
        print("ReactionGame")

    def update(self):
        print ("--- reactionGame update")
        self.parent.screen.drawText("Reaction Game", 0, 0)

        if self.timer.check():
            print(1)
            self.state = not self.state
            
            self.can_press_button = self.state

            if self.state:
                print(2)
                time_to_change = 2
                self.timer.set(time_to_change*1000)
                
                self.parent.screen.drawRectangle(0, 0, 128, 64)
            else:
                print(3)
                time_to_change = random.randint(5, 16)
                self.timer.set(time_to_change*1000)
                


        if self.can_press_button:
            buttons = self.parent.buttons.getPressedButtons()
            if buttons[0] == 1:
                self.parent.wifi.completeMinigame(self.parent.badgeUID)
                self.parent.isMinigameCompleted = True
                self.parent.lastMinigame = ReactionGame
                self.parent.gotoIdleGame()
