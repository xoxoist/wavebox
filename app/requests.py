from pydantic import BaseModel


class RequestCreateFoo(BaseModel):
    foo_first_name: str
    foo_last_name: str


class RequestCreateBar(BaseModel):
    bar_first_name: str
    bar_last_name: str
