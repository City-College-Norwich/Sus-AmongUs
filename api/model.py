class Model:
    def __init__(self):
        self.uids = {"fakeKey":"testValue"}
        self.totalMinigames = 10
        self.completedMinigames = 0
        self.state = "Game_Running"
        pass

    def getTagName (self, uid):
        return self.uids[uid]      
      
    def callHomepage(self):
        return "hello"

    def minigameComplete(self, scannerId):
        self.completedMinigames += 1

    def keepAlive(self):
        if self.completedMinigames >= self.totalMinigames:
            self.state = "Game_Ended"
        
        if self.state = "Game_Ended":
            return "Game_Ended"
