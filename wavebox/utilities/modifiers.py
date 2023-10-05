class BaseModelFuncs:
    @staticmethod
    def to_kebab_case(header_value: str) -> str:
        return ''.join(['-' + i.capitalize() if i.isupper() else i for i in header_value]).lstrip('-')

    @staticmethod
    def to_snake_case(headers: dict) -> dict:
        return {key.replace("-", "_"): value for key, value in headers.items()}
