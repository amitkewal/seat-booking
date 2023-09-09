from typing import Dict, List

from utils import CamelModel


class User(CamelModel):

    name: str
    email: str
    department: str
    location: str
    seat_allocation: list
    mobile_no: str
    user_id: str
    password: str

class UserCred(CamelModel):
    email: str
    password: str


class UserResponse(CamelModel):
    message : str


class MySeats(CamelModel):
    name: str
    email: str
    department: str
    location: str
    seats_shiftes1: list
    seats_shiftes2: list
    mobile_no: str


class SeatUpdate(CamelModel):
    name: str
    seat_no: str
    booking_id: str
    day:str
    shift:str


class SeatRequest(CamelModel):
    department: str
    location: str
    date: str
    shift: str

class SeatDelete(CamelModel):
    name:str
    booking_id:str