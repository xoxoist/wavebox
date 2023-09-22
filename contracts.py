import json
from dataclasses import dataclass, asdict


class JsonContract:
    @staticmethod
    def to_json(self) -> str:
        return json.dumps(asdict(self), indent=2)
