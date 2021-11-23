
from flask import Flask, request
from model import Model
app = Flask(__name__)

model = Model()


@app.route("/")
def home():
    return model.callHomepage()

@app.route
def setMaxMiniGames():
    return model.setMaxMiniGames(request.args["count"])

@app.route("/StartGame")
def startGame():
    return model.startGame()

@app.route("/requestStation")
def requestStation():
    return model.requestStation()


@app.route("/getTagName")
def getTagName():
    return model.getTagName(request.args["uid"])


@app.route("/minigameComplete")
def minigameComplete():
    return model.minigameComplete(request.args["scannerId"])


@app.route("/keepAlive")
def keepAlive():
    return model.keepAlive()
  

  @app.route("/killPlayer")
def killPlayer():
    args = request.args
    return model.killPlayer(args["myUID"], args["victimUID"])


@app.route("/startVote")
def startVote():
    return model.startVote()

@app.route("/registerUser")
def registerUser():
    args = request.args
    return model.registerUser(args["badgeUID"])

  
@app.route("/sabotage")
def sabotage():
    return model.sabotage(request.args["sabotageType"])

@app.route("/sabotageCompleted")
def sabotageCompleted():
    args = request.args
    return model.sabotageCompleted(args["badgeUID"])


@app.route("/voteTally")
def voteTally():
    args = request.args
    return model.voteTally(args["badgeUID"], args["myUID"])

@app.route("/isAlive")
def isAlive():
    args = request.args
    return model.isAlive(args["badgeUID"])



@app.route("/isImposter")
def isImposter():
    args = request.args
    return model.isImposter(args['uid'])


@app.route("/AutoDownloader/GetFileList")
def getFileList():
    return model.getFileList()

@app.route("/AutoDownloader/GetFile")
def getFile():
    args = request.args
    return model.getFile(args['fileName'])

@app.route("/initiateVote")
def initiateVote():
    return model.initiateVote()

@app.route("/voteTimeEnd")
def voteTimeEnd():
    return model.voteTimeEnd()

if __name__ == '__main__': app.run(host='0.0.0.0')
