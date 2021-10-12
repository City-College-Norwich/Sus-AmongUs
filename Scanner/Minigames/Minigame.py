from Minigames.GoodGuyGame import GoodGuyGame
from Minigames.Sabotage1 import Sabotage1



class Minigame:
    def __init__(self, parent):
        self.parent = parent

    def update(self):
        pass

    def alertsFromServer(self, alerts):
        if 'GameStarted' in alerts:
            self.parent.currentMiniGame = GoodGuyGame()

        if 'Crewmate_Win' in alerts:
            self.parent.currentMiniGame = GoodGuyGame()
            self.parent.currentMiniGame.state = 1  # Crewmate win

        elif "Impostor_Win" in alerts:
            self.parent.currentMiniGame = GoodGuyGame()
            self.parent.currentMiniGame.state = 2  # Impostor win

        if 'Sabotaged' in alerts:
            sabotage_type = self.parent.wifi.send_request("getSabotageType")

            if sabotage_type == 1:
                self.parent.currentMiniGame = Sabotage1(parent)
            elif sabotage_type == 2:
                self.parent.currentMiniGame = Sabotage2(parent)
            else:
                self.parent.currentMiniGame = Sabotage3(parent)
