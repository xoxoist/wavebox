from pydantic import BaseModel


class ResponseBase(BaseModel):
    response_code: str | None = None
    response_message: str | None = None
