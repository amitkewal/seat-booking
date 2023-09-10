from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from asgi_correlation_id import CorrelationIdMiddleware

import logging
# setup loggers
logging.config.fileConfig('./core/logging.conf', disable_existing_loggers=False)

# get root logger
logger = logging.getLogger(__name__)  

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(CorrelationIdMiddleware)


@app.get("/")

def welcome():
    logger.info("logging from the root logger")
    return "kya re bhai!!!!"

@app.get("/hi")
def hii():
    return "hiiiiiii bhai BHAK!!"

from controller import *