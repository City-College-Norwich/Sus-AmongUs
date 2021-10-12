from GoodGuyGame import GoodGuyGame


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
            pass

