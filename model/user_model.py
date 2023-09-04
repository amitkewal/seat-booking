from bson.json_util import dumps, loads, json
import uuid
from fastapi import HTTPException

from pymongo import MongoClient
from service.mail_service import mail_service
from model.seat_model import seat_model
from dateutil import parser
from datetime import datetime

class user_model():
    def __init__(self):
        client = MongoClient('127.0.0.1', 27017)
        try:
            client.seatqqq_booking.command('ping')
            print("Pinged your seatqqqq_booking deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        self.db = client['seatko']
        # self.collection = self.db['user']

    def verify_user(self, email):
        result = self.db.user.find_one({"email":str(email)},{'_id':0})
        print("|||||resulttttt", result)
        if result:
            raise HTTPException(status_code=400, detail="Username already exists")
        else:
            return True

    def user_signup(self, user):
        result = self.db.user.insert_one(user)
        inserted_id = str(result.inserted_id)
        return {"message": "User registered successfully", "user_id": inserted_id}


    def user_add_booking(self, user):
        try:
            # print("||%%%%%%%%%%%%%%", user)
            seats = user['seat_allocation']
            mail_seats = ", "
            mail_date = ","
            new_seat = list()
            for seat in seats:
                # seat = seat.dict()
                # print("########", seat)
                seat["booking_id"] = str(uuid.uuid1())
                new_seat.append(seat)
                mail_seats += (seat.get("seat_no"))
                mail_date += (seat.get("day"))
            # print(user['name'],"########", new_seat)

            book_seat = self.db.user.update_one({"name":user['name']}, {"$push":{"seat_allocation": {"$each":new_seat}}})
            # if book_seat.modified_count == 0:
            #     return None
            updated_data = self.get_my_booking(user.get("name"))

            # print("@@@", updated_data)
            final_data = seat_model()
            final_data.update_seats(updated_data)
            # print("______________-------------------", mail_seats)
            mobj = mail_service()
            res = mobj.send_mail(user['name'], mail_seats[1:], mail_date[1:])
            # print("MMMMMMMMMMMMM", res)
            return True
        except Exception as e:
            
            print(e)
            return False

    def get_my_booking(self,name):
        try:
            # res = self.db.user.insert_one(data)

            res = self.db.user.find({"name":str(name)},{'_id':0})
            final_response = dict(res[0])
            # print("%%%%%%%%%%%%%%%%", final_response)

            return final_response
  
        except Exception as e:
            print(e)

    def get_user_data(self,username):
        try:
            current_date = datetime.today()
            days = list()
            # res = self.db.user.insert_one(data)
            res = self.db.user.find({"name":username},{'_id':0})
            final_response = dict(res[0])
            for seat in final_response.get("seat_allocation"):
                seat_day = parser.parse(seat.get("day"))
                if str(current_date.month) == str(seat_day.month):
                    days.append(seat_day.day)
            final_response["calendar_highlights"] = days
            return final_response
  
        except Exception as e:
            print(e)

    def get_my_booking_calendar(self,user_id,s_date,e_date):
            from datetime import date, timedelta
            from datetime import datetime
            seat_details = list(self.db.user.find({"user_id":user_id},{"_id":0,"name":0,"department":0,"location":0,"mobile_no":0,"user_id":0}))
            print(seat_details)
            s = seat_details[0].get("seat_allocation")
            print(s)
            for seat,info in s.items():
                print(seat , ":::::", info)
            my_list = []
            ## create a dict of days
            def daterange(start_date, end_date):
                for n in range(int((end_date - start_date).days)+1):
                    yield start_date + timedelta(n)
            s_date_list = s_date.split('-')
            e_date_list = e_date.split('-')
            start_date = date(int(s_date_list[0]), int(s_date_list[1]), int(s_date_list[2]))
            end_date = date(int(e_date_list[0]), int(e_date_list[1]), int(e_date_list[2]))
            for single_date in daterange(start_date, end_date):

                my_list.append(single_date.strftime("%Y-%m-%d"))

                print("|||||||",single_date.strftime("%Y-%m-%d"))
            my_dict = dict.fromkeys(my_list)


            #filling the dic values by seat number

            for date in my_dict.keys():
                # my_json={}
                # my_json.values
                for seat,info in s.items():
                    for i in info:
                        if str(i['day']) == str(date):
                            print(i['day'],"##########", date,"||||||||||||", s[seat])
                            my_dict[date] = seat
            return my_dict
    
    def user_update_booking(self,seat):
        try:

            update_data = dict()
            update_data["booking_id"] = seat.get("booking_id")
            update_data["day"] = seat.get("day")
            update_data["seat_no"] = seat.get("seat_no")
            update_data["shift"] = seat.get("shift")
            # update_data['name'] = seat.get('name')
            # print("$$$$$$",update_data, seat)
            update_request = self.db.user.update_one({"name":seat.get("name"), "seat_allocation.booking_id":seat.get("booking_id")}, {"$set": {"seat_allocation.$":update_data}})
            
            if update_request.modified_count == 0:
                return False
            updated_data = self.get_my_booking(seat.get("name"))

            # print("@@@", updated_data)
            final_data = seat_model()
            final_data.update_seats(updated_data)
            return update_data
        except Exception as e:
            print(e)
            return False

    def user_delete_booking(self,seat):
        try:

            seat_obj = seat_model()
            seat_obj.delete_seats(self.get_my_booking(seat.get("name")),seat.get("booking_id"))
            

            update_request = self.db.user.update_one({"name":seat.get("name"), "seat_allocation.booking_id":seat.get("booking_id")}, {"$pull": {"seat_allocation":{"booking_id":seat.get("booking_id")}}})
            
            if update_request.modified_count == 0:
                return False

            return True
            
        except Exception as e:
            print(e)
            return False