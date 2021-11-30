import random
import csv
import json
import os, sys

from TimerHelper import TimerHelper

GAME_STARTING = 1
GAME_RUNNING = 2
GAME_ENDED = 3
CREWMATE_WIN = 4
IMPOSTER_WIN = 5
class Player:
    def __init__(self,username):
        self.alive = True
        self.team = ""
        self.joinedVote = False
        self.hasVoted = False
        self.votesAgainst = 0
        self.username = username


class Model:
    def __init__(self):

        with open('RFIDMap.csv', mode='r') as csvfile:
            reader = csv.reader(csvfile)
            self.uids = {row[0]: row[1] for row in reader}  # creates csv file containing players

        #    '''
        #   {this is what i shere: this is here}
        #  '''
        self.totalMinigames = 6  # how many games a player has
        self.completedMinigames = 0  # how many games the player has completed
        self.state = GAME_STARTING

                      # card ID:   [team,   alive/dead, votecounter, hasVoted, playerID]
        self.players ={}

        self.crewmateCount = 0  # total count of current crewmates in a game
        self.imposterCount = 0  # total number of current imposters in a game

        self.maxImposters = 1

        self.sabotaged = False  # these reffer to things to help with saboutages , this one is the alert

        self.sabotage_type = 0
        self.sabotage_timer = TimerHelper()
        self.sabotage_participants = set()

        self.totalVote = 0
        self.voting = False
        self.initiateVoteCounter = 0

        self.joinVoteTimer = TimerHelper()
        self.votingTimer = TimerHelper()
        self.votingRunning = False

        self.MEETINGCOOLDOWN_AMOUNT = 20000
        self.meetingCooldown = TimerHelper()
        self.voteType=None
        self.lastVotedOut = None


        self.meetingsLeft = 3

    def getTagName(self, uid):  # use to find badge id of player
        if uid in self.uids.keys():
            return self.uids[uid]
        else:
            return "No tags found"

    def setMaxMiniGames(self, cnt):
        self.totalMinigames = int(cnt)
        return "okay"

    def startGame(self):  # takes game into active and starts up (this needs to be affected for lobby)
        players = list(range(len(self.players.keys())))
        for i in range(self.maxImposters):
            imposter = players.pop(random.randint(0, len(players) - 1))
            self.players[list(self.players.keys())[imposter]].team = "Imposter"
    
            self.imposterCount += 1

        for crewmate in players:
            self.players[list(self.players.keys())[crewmate]].team = "Crewmate"
        self.crewmateCount = len(players)

        self.state = GAME_RUNNING
        return "okay"

    def callHomepage(self):  # network test
        return "hello"

    def requestStation(self):  # chooses a random staton
        return "station" + str(random.choice(range(1, 6)))

    def minigameComplete(self, scannerId):  # adds to completed minigame for crewmate
        self.completedMinigames += 1
        return "Okay"

    def keepAlive(self):  # loop for alerts
        alerts = {}
        if self.state == GAME_RUNNING:
            alerts["GameRunning"] = True
            if self.sabotaged:
                alerts["Sabotaged"] = self.sabotage_type #where it checks for sabotage
                if self.sabotage_type == 1 or self.sabotage_type == 3:
                    alerts["SabotagedStation"] = self.sabotaged_station

                if self.sabotage_timer.check():  # ends game if timer runs out
                    self.state = IMPOSTER_WIN

            elif self.voting == True: #starts vote

                if not self.votingRunning:
                    # if the timer is hit, we will kill every player that hasnt joined the voting process
                    if self.joinVoteTimer.check():
                        for key in self.players.keys():
                            if not self.players[key].joinedVote:
                                self.executePlayer(key)

                        self.voting = False
                    else:
                        alerts["Start_Voting"] = self.voteType
                else:
                    if self.votingTimer.check():
                        self.endVote()
                    else:
                        alerts["Start_Voting"] = self.voteType
                        alerts["Initiate_Voting"] = True
            
            if self.lastVotedOut != None:
                alerts["Last_Voted"]=self.lastVotedOut.team()
            
            if self.imposterCount == 0 or self.totalMinigames == self.completedMinigames: #win states 

                self.state = CREWMATE_WIN
            elif self.crewmateCount == self.imposterCount:
                self.state = IMPOSTER_WIN

        if self.state == IMPOSTER_WIN:
            alerts["Winner"] = "Imposters"
        elif self.state == CREWMATE_WIN:
            alerts["Winner"] = "Crewmates"

        return json.dumps(alerts)

    def killPlayer(self, selfUID, victimUID):  # defines murder
        killer = self.players[selfUID]
        victim = self.players[victimUID]
        if killer.alive == True and victim.alive == True:
            if killer.team == "Imposter" and victim.team == "Crewmate":
                return self.executePlayer(victimUID)
        return "error"

    # This function is used to set the killed player to be dead and also removes one from their teams count.
    def executePlayer(self, victimUID):
        self.players[victimUID].alive = False
        if self.players[victimUID].team == "Crewmate":
            self.crewmateCount -= 1
        else:
            self.imposterCount -= 1
        return "ok"

      
    def startVote(self): #starts voting game 

        self.totalVote = 0
        self.initiateVoteCounter = 0
        
        for key in self.players.keys():
            self.players[key].votesAgainst = 0
            self.players[key].hasVoted = False
            self.players[key].joinedVote = False

        self.joinVoteTimer.set(60000)
        self.voting = True
        return "ok"

    def setVoteType(self, type):
        self.voteType = type
        return "ok"


    def joinVote(self,badgeUID): #Ensure everyone is ready to vote. Further verification needs to be added.
        self.players[badgeUID].joinedVote = True

        self.initiateVoteCounter += 1
        if self.initiateVoteCounter == (self.imposterCount + self.crewmateCount):
            if self.votingRunning == False:
                self.votingTimer.set(60000)
                self.votingRunning = True
        return "ok"
     
    def registerUser(self,badgeUID):#this is where players are assigned 
        if badgeUID in self.players.keys(): 
            return "User is already Registered!"

        self.players[badgeUID] = Player(len(self.players.keys())+1)
        self.uids[badgeUID] = "playerId"
        return "Okay"

    def sabotage(self,
                 sabotageType):  # defines basic sabotage value (second one needs to be made for player reset as the limit is a static number not a timer)
        if self.sabotaged == True:
            pass
        else:
            self.sabotaged = True
            self.sabotage_type = sabotageType
            if self.sabotage_type == 1:
                self.sabotaged_station = self.requestStation()
                self.sabotage_timer.set(60000)
            elif self.sabotage_type == 3:
                self.sabotaged_station = self.requestStation()
                self.sabotage_timer.set(90000)
        return "ok"

    def sabotageCompleted(self, badgeUID):  # makes it so one person cant act as two people in the sbotage game
        # handling sabotage 1 logic
        if self.sabotage_type == 1:
            if badgeUID in self.sabotage_participants:
                pass
            else:
                self.sabotage_participants.add(badgeUID)
                if len(self.sabotage_participants) == 2:
                    self.sabotaged = False
                    self.sabotage_participants = set()
        elif self.sabotage_type == 3:
            self.sabotaged = False

    def voteTally(self, badgeUID, myUID):
        self.players[badgeUID].votesAgainst = self.players[badgeUID].votesAgainst + 1
        self.players[myUID].hasVoted = 1
        self.totalVote += 1
        if self.totalVote == (self.crewmateCount + self.imposterCount):
            return self.endVote()
        return "ok"

    def endVote(self):
        if self.voting == True:
            self.voting = False
            voteArray = []
            for key in self.players:
                addPlayer = []
                if self.players[key].alive == True:
                    addPlayer.append(key)
                    addPlayer.append(self.players[key].votesAgainst)
                    voteArray.append(addPlayer)
            sorted(voteArray, key=lambda x: x[1], reverse=True)
            playerID = voteArray[0][0]
            
            if self.voteType=='meeting':
                self.meetingCooldown.set(self.MEETINGCOOLDOWN_AMOUNT)
                
        if voteArray[0][1] != voteArray[1][1]:
            self.lastVotedOut = self.players(playerID)
            #return json.dumps(list(playerID,self.players[playerID]))
        if voteArray[0][1] == voteArray[1][1]:
            return "draw"

        #TODO: The player ejected will need to be returned and consequently printed to the screen of every scanner.
        
    def isAlive(self, badgeUID):#checks to see if player is alive 
        if self.players[badgeUID].alive:
            return "yes"
        return "no"

    def isImposter(self, uid):  # checks if player is imposter
        if self.players[uid][0] == "Imposter":
            return "True"
        return "False"

    def getPlayers(self):
        return json.dumps(self.players)

    fileList = [  # list of relevent files
        "App.py",
        "Buttons.py",
        "Rfid.py",
        "Screen.py",
        "TimerHelper.py",
        "Wifi.py",
        "boot.py",
        "Minigames/DownloadGame.py",
        "Minigames/GoodGuyGame.py",
        "Minigames/IdBadge.py",
        "Minigames/ImposterGame.py",
        "Minigames/Minigame.py",
        "Minigames/ReactionGame.py",
        "Minigames/RecordTemperatureGame.py",
        "Minigames/Sabotage1.py",
        "Minigames/Sabotage3.py",
        "Minigames/StartupGame.py",
        "Minigames/UploadGame.py",
        "Minigames/VotingGame.py"]

    def getFileList(self):  # gets list of files
        return json.dumps(self.fileList)

    def getFile(self, fileName):  # gets the name of a file
        currentdir = os.path.dirname(os.path.realpath(__file__))
        parentdir = os.path.dirname(currentdir)
        scannerdir = os.path.join(parentdir, "Scanner")

        if fileName in self.fileList:  # returns file through network
            with open(os.path.join(scannerdir, fileName), "r") as f:
                file = f.read()
            return file
        return ""

    def checkMeeting(self):
        if self.meetingCooldown.check() and self.meetingsLeft != 0:
            self.meetingsLeft-=1
            return True
        else:
            return False
            

