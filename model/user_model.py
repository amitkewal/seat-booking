from bson.json_util import dumps, loads

from pymongo import MongoClient
class user_model():
    def __init__(self):
        client = MongoClient('127.0.0.1', 27017)
        try:
            client.seatqqq_booking.command('ping')
            print("Pinged your seatqqqq_booking deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        self.db = client['seat_booking']
        # self.collection = self.db['user']

    def user_sign_up(self, data):
        #business logic
        try:
            # res = self.db.user.insert_one(data)
            res = self.db.user.update_one({"name":data['name']},{"$set": data}, upsert=True)

            print(res.raw_result)

            return "this is sign up model"
  
        except Exception as e:
            print(e)
            return "this is hhhhhhh"

