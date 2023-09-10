from bson.json_util import dumps, loads, json
import uuid
# from pymongo import MongoClient
from model import db

class seat_model():
    def __init__(self):
        print("Inside Seat Model...")

    def update_seats(self, data):
        seats_shift1 = []
        seats_shift2 = []
        seat_allocation = data.get("seat_allocation")
        for seat in seat_allocation:
            # update_data["seat_no"] = seat.get("seat_no")
            # update_data["date"] = data.get("day")
            if seat.get("shift") == "shift1":
                 
                seats_shift1.append({"seat_no":seat.get("seat_no"),"name":data.get("name"),"date":seat.get("day"), "shift":"shift1", "booking_id":seat.get("booking_id")})
            else:
                print("helooo")
                seats_shift2.append({"seat_no":seat.get("seat_no"),"name":data.get("name"),"date":seat.get("day"), "shift":"shift2", "booking_id":seat.get("booking_id")})

            print("!!!!!!!!!!!!!!", seats_shift1)
            print("!!!!!!!!!!!!!!", seats_shift2)
            print("!!!!!!!!!!!!!!", data.get("location"))
        # update_request = db.user.update_one({"name":seat.get("name"), "seat_allocation.booking_id":seat.get("booking_id")}, {"$set": {"seat_allocation.$":update_data}})

        update_request = db.seats.update_one({"location":data.get("location")}, {"$set": {"seats_shift1":seats_shift1,"seats_shift2":seats_shift2}})


        return "what"


    def get_available_seats(self, data):
        print("+++++++++++++++++++", data)

        update_response= db.seats.find_one({"location":data.get("location")})
        print("+++++++++++++++++++", update_response)
        print("+++++++++++++++++++", update_response.get("location"))
        if data.get("shift") == "shift1":
            seat_iterator = "seats_shift1"
        else:
            seat_iterator = "seats_shift2"

        seats_shift_res = []
        print("!!!!!!!---", update_response[seat_iterator])

        for seat in update_response[seat_iterator]:
            print("!!!!!!!---======", data["date"], seat.get("date"))
            if seat.get("date") == data["date"]:
                seats_shift_res.append({"seatNumber":seat.get("seat_no"),"dept":data.get("department")})
        
        print("&&&&&&&&&", seats_shift_res)
        return seats_shift_res
    
    def delete_seats(self,user,booking_id):
        try:
            shift = None 
            for seat in user.get("seat_allocation"):
                if seat.get("booking_id") == booking_id:
                    shift = seat.get("shift")

            if shift == "shift1":
                delete_seat = db.seats.update_one({"location":user.get("location"), "department":user.get("department")}, {"$pull": {"seats_shift1":{"booking_id":booking_id}}})
            else:
                delete_seat = db.seats.update_one({"location":user.get("location"), "department":user.get("department")}, {"$pull": {"seats_shift2":{"booking_id":booking_id}}})

                            
            
        except Exception as e:
            print(e)