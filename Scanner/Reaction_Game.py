from Minigame import Minigame
import random
import time
import Buttons
import WiFi

class Reaction_Game:
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.parent = parent

    def update():
        pass

    def alertFromServer(self, alert):
        if alert == 'GameStarted':
            self.parent.currentMiniGame = Reaction_Game()

    def reaction_game(self.parent.rfid):
        self.can_press_button = False
        time_to_change = Random.randint(5,16)
        self.time_passed = time.ticks_ms()/1000

        if self.time_passed == time_to_change:
            display.fill(1)
            self.can_press_button = True

    def Reaction_Button_Pressed(self):
        time_to_change = 2
        self.time_passed = time.ticks_ms()/1000

        if self.time_passed == time_to_change:
            display.fill(0)
            self.can_press_button = False
            #Game starts over

        elif self.can_press_button == True:
            Buttons.getPressedButton(self)
            if self.__button0.value() == 1:
                WiFi.send_request(self, "Reaction_Game Complete")
