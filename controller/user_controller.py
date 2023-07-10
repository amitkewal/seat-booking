from main import app

from fastapi import FastAPI
from schemas import User
from model.user_model import user_model


obj = user_model()
@app.post("/add_user")
def user_signup_controller(user : User):
    print("||||||||||||||||||||||||", user)
    print("||||||||||||||||||||||||")

    print(user)
    return obj.user_sign_up(user.model_dump())
