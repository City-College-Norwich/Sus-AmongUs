
from flask import Flask
from model import model
app = Flask(__name__)

model = Model()

@app.route("/")
def home():
    return model.callHomepage()
    

@app.route("/getTagName")
def getTagName():
    args = request.args

    return model.getTagName(args["uid"])


