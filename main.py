from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def welcome():
    return "kya re bhai!!!!"

@app.get("/hi")
def hii():
    return "hiiiiiii bhai BHAK!!"

from controller import *