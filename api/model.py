class Model:
    def __init__(self):
        self.totalMinigames = 10
        self.completedMinigames = 0
        self.state = "Game_Running"
        pass

    def callHomepage(self, scannerId):
        return "hello"

    def minigameComplete(self, scannerId):
        self.completedMinigames += 1
        

    def alertFromServer(self, alert):
        pass

    def keepAlive(self):
        if self.completedMinigames >= self.totalMinigames:
            self.state = "Game_Ended"
        
        if self.state = "Game_Ended":
            return "Game_Ended"