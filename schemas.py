from typing import Dict, List

from utils import CamelModel


class User(CamelModel):

    name: str
    email: str
    department: str
    location: str
    seat_allocation: list
    mobile_no: str


class UserResponse(CamelModel):
    message : str