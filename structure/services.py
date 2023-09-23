from abc import ABC, abstractmethod
from pydantic import BaseModel


class Services(ABC):
    """
    "Services" this represents basic function for business logic like
    request serialization and response deserialization before passed
    to the controller abstraction, generally other business logic
    that inherits this class will have function serialize, manipulator
    and deserialize.
    """

    @abstractmethod
    def _validate(self): raise NotImplemented

    @abstractmethod
    def _logics(self) -> (BaseModel, int): raise NotImplemented

    @abstractmethod
    def retrieve(self) -> (BaseModel, int): raise NotImplemented
