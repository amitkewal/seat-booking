# Steps to follow
## Fast API for seat booking

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Seatko is a product for seat booking. This repo contains

- Backend API in python
- FASTAPI used
- MongoDB

## Features
------Plugins
## Tech

## Plugins


| Plugin | README |
| ------ | ------ |
| pymongo | [https://github.com/mongodb/mongo-python-driver/blob/master/README.rst][PlDb] |
| uvicorn | [https://github.com/encode/uvicorn/blob/master/README.md] [PlGh] |
| fastapi | [https://github.com/tiangolo/fastapi/blob/master/README.md][PlGd] |
| boto3 | [https://github.com/boto/boto3/blob/develop/README.rst][PlOd] |


## Development

Follow following steps:
```sh
git clone https://github.com/amitkewal/seat-booking.git
cd seat-booking
python -m venv venv
```

Set Virtual Environment:

Window:

```sh
python -m venv venv
Set-ExecutionPolicy Unrestricted -Scope Process
.\venv\Scripts\Activate
```

Mac:

```sh
python -m venv venv
source ./myvenv/bin/activate
```

#### Building source

Install dependencies
```sh
pip install -r requirements.txt 
```


#### Install mongo via docker on win or ubuntu:

```sh
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-community-with-docker/

command to run the mongo image. You need to do port forward:
docker run --name mongo -p 27017:27017 -d mongodb/mongodb-community-server:latest
```

#### Install mongo on mac(via docker its now working let me know if got any solution):

```sh
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/
```

#### Then start the app:
```sh
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```
## Add users:

```sh
curl --location 'http://127.0.0.1:8080/sign_up' \
--header 'Content-Type: application/json' \
--data-raw '{
        "name": "amitk",
        "password": "######",
        "email"   : "amit.iitr.cs@gmail.com",
        "department": "cse",
        "location": "pune",
        "seatAllocation": [],
        "mobileNo": "+91900000000",
        "userID": "123"

    }'
```

#### #insert seats documents in seats collection
 
```sh
db.seats.insert({"location":"pune","department":"it","floor":14,"total":50,"seats_shift1":[],"seats_shift2":[],"map":"abc.jpg"})

db.seats.insert({"location":"manila","department":"it","floor":10,"total":51,"seats_shift1":[],"seats_shift2":[],"map":"xyz.jpg"})

```

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
