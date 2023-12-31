from main import app
# from fastapi import FastAPI
# from fastapi import FastAPI, HTTPException, Form
from schemas import User,SeatUpdate,SeatDelete, UserCred
from model.user_model import user_model
from fastapi.responses import JSONResponse
from passlib.hash import pbkdf2_sha256
import logging
logging.config.fileConfig('./core/logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)  


obj = user_model()

# user login api
@app.post("/login")
async def login_user(userCred: UserCred):
    logging.info(f"Controller :: login api called for {userCred.email}")
    return obj.user_login(userCred)

# Create a user registration endpoint
@app.post("/sign_up")
async def register_user(user: User):
    # Check if the username already exists in the database
    if obj.verify_user(user.email):
        # Hashing the password
        hashed_password = pbkdf2_sha256.hash(user.password)  
        # Create user payload
        new_user = {
            "username": user.name,
            "password": hashed_password,
            "email"   : user.email,
            "department": user.department,
            "location": user.department,
            "seat_allocation": user.seat_allocation,
            "mobile_no": user.mobile_no,
            "user_id": user.user_id

        }
        return obj.user_signup(new_user)


@app.post("/book_seats")
def user_book_seats_controller(user : User):
    # print("||||||||||||||||||||||||", user)
    # print("||||||||||||||||||||||||++++++")

    # print(user.model_dump())
    model_response = obj.user_add_booking(user.dict())
    if model_response:
        return JSONResponse(content={"message":"seat booked successfully"})
    else:
        # return JSONResponse(content={"message":"seat booked"})
        return JSONResponse(content={"message": "seat booked failed"}, status_code=404)

@app.get("/get_user/{username}")
def get_user_info(username: str):
    model_response = obj.get_user_data(username)
    return JSONResponse(content=model_response)



@app.get("/get_bookings/{user_id}")
def user_get_my_booking(user_id: str):
    model_response = obj.get_my_booking(user_id)
    if model_response:
        return JSONResponse(content=model_response)
    else:
        return JSONResponse(content={"message": "bookings not found"}, status_code=404)

@app.get("/get_bookings_calendar/")
def user_get_my_booking_calendar(user_id: str,start_date,end_date):
    model_response = obj.get_my_booking_calendar(user_id,start_date,end_date)
    return JSONResponse(content=model_response)

@app.put("/update_bookings")
def user_update_booking(seat: SeatUpdate):
    model_response = obj.user_update_booking(seat.dict())
    if model_response:
        return JSONResponse(content={"message":"bookings updated successfully", "data":model_response})
    else:
        return JSONResponse(content={"message":"bookings failed to update", "data":{}},status_code=404)

@app.delete("/delete_bookings")
def user_delete_booking(seat: SeatDelete):
    model_response = obj.user_delete_booking(seat.dict())
    if model_response:
        return JSONResponse(content={"message":"bookings deleted successfully"})
    else:
        return JSONResponse(content={"message":"bookings failed to delete"}, status_code=404)



