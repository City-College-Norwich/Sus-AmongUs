from Minigame import Minigame
from TimeHelper import TimeHelper

class ImposterGame(Minigame):
    def __init__(self, parent):
        Minigame.__init__(self, parent)
        self.timer = TimeHelper()
        self.cooldown = self.timer.set(60000)
    
    def update(self):
        if self.timer.check() == self.cooldown:
            buttons = self.parent.buttons.getPressedButtons()
            if buttons[0] == 1:
                self.wifi.sendRequest("sabotage?sabotageType=1")
            elif buttons[1] == 1:
                self.wifi.sendRequest("sabotage?sabotageType=2")
            elif buttons[2] == 1:
                self.wifi.sendRequest("sabotage?sabotageType=3")

    def alertsFromServer(self, alerts):
        Minigame.alertsFromServer(self, alerts)
        if 'Sabotaged' in alerts:
            #Having the cooldown set here to 120 seconds will allow for the
            #60 seconds to complete the sabotage task (Crewmates) and also
            #the default 60 second cooldown for sabotages
            self.cooldown(120000)
