from itertools import tee
from io import StringIO

from bson.objectid import ObjectId
from fastapi.exceptions import HTTPException
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel


async def http_exception_handler(req: Request, exc: HTTPException) -> JSONResponse:
    if exc.headers is None:
        return JSONResponse(
            {"detail": exc.detail},
            status_code=exc.status_code
        )
    return JSONResponse(
        {"detail": exc.detail, "error": exc.headers.get("x-error")},
        headers=exc.headers,
        status_code=exc.status_code
    )


def to_camel(var: str):
    all_upper_words = {"url", "id"}
    camel_var = StringIO()

    for index, s in enumerate(var.split("_")):
        if index == 0:
            camel_var.write(s)
        elif s in all_upper_words:
            camel_var.write(s.upper())
        else:
            camel_var.write(s.title())

    return camel_var.getvalue()


def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


class ObjectIdHelper(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class CamelModel(BaseModel):
    class Config:
        alias_generator = to_camel
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: lambda i: str(i),
        }
