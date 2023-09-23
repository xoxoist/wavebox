from pydantic import BaseModel


def _to_kebab_case(header: str) -> str:
    return ''.join(['-' + i.capitalize() if i.isupper() else i for i in header]).lstrip('-')


def _to_snake_case(header: dict) -> dict:
    return {key.replace("-", "_"): value for key, value in header.items()}


class HeaderBase(BaseModel):
    ContentType: str = None
    RequestId: str = None

    class Config:
        alias_generator = _to_kebab_case

    @classmethod
    def from_dict(cls, header_dict):
        return cls(**_to_snake_case(header_dict))
