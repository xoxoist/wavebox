from pydantic import BaseModel
from utilities.modifiers import BaseModelFuncs


class HeaderBase(BaseModel):
    ContentType: str
    RequestId: str

    class Config:
        alias_generator = BaseModelFuncs.to_kebab_case

    @classmethod
    def from_dict(cls, header_dict):
        return cls(**BaseModelFuncs.to_snake_case(header_dict))
