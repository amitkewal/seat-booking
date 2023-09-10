from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
try:
    client.seatqqq_booking.command('ping')
    print("Pinged your seatqqqq_booking deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db = client['seatko']
