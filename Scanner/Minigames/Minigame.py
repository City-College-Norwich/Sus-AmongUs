from IdleGame import IdleGame


class Minigame:
    def __init__(self, parent):
        self.parent = parent

    def update(self):
        pass

    def alertsFromServer(self, alerts):
        if 'GameStarted' in alerts:
            self.parent.currentMiniGame = IdleGame()

        if 'Crewmate_Win' in alerts:
            self.parent.currentMiniGame = IdleGame()
            self.parent.currentMiniGame.state = 1  # Crewmate win

        elif "Impostor_Win" in alerts:
            self.parent.currentMiniGame = IdleGame()
            self.parent.currentMiniGame.state = 2  # Impostor win
