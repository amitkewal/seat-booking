from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "kya re bhai!!!!"

@app.route("/hi")
def hii():
    return "hiiiiiii bhai BHAK!!"

from controller import *