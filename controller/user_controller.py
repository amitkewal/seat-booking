from app import app
from flask import request

from model.user_model import user_model


obj = user_model()
@app.route("/add_user", methods = ['POST'])
def user_signup_controller():
    print("||||||||||||||||||||||||")
    data = request.json
    print("||||||||||||||||||||||||")

    print(data)
    return obj.user_sign_up(data)