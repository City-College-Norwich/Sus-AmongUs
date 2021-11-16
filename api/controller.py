
from flask import Flask, request
from model import Model
app = Flask(__name__)

model = Model()


@app.route("/")
def home():
    return model.callHomepage()


@app.route("/StartGame")
def startGame():
    res = "000"
    try:
        res = model.startGame()
    except(ValueError):
        return "500: Value Error"
    except:
        return "500: N/A"   

@app.route("/requestStation")
def requestStation():
    return model.requestStation()


@app.route("/getTagName")
def getTagName():
    args = request.args
    return model.getTagName(args["uid"])


@app.route("/minigameComplete")
def minigameComplete():
    args = request.args
    return model.minigameComplete(args["badgeUID"])


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
    args = request.args
    return model.sabotage(args["sabotageType"])


@app.route("/getSabotageType")
def getSabotageType():
    return model.sabotage_type()


@app.route("/sabotageTimeout")
def sabotageTimeout():
    return model.sabotageTimeout()


@app.route("/sabotageCompleted")
def sabotageCompleted():
    return model.sabotageCompleted()


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

if __name__ == '__main__': app.run(host='0.0.0.0')
