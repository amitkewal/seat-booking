from main import app

# from fastapi import FastAPI
from schemas import SeatRequest
from model.seat_model import seat_model

# from fastapi.responses import JSONResponse

obj = seat_model()
@app.post("/get_seats")
def get_seats(seat : SeatRequest):
    print("||||||||||||||||||||||||", seat)
    print("||||||||||||||||||||||||++++++")

    print(seat.dict())

    # return "hii"
    final = obj.get_available_seats(seat.dict())
    return final 