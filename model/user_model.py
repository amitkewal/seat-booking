
from pymongo import MongoClient
class use_model():
    def __init__(self):
        client = MongoClient('localhost', 27017)
    def user_sign_up(self):
        #business logic
        return "this is sign up model"