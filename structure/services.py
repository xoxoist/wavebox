from abc import ABC, abstractmethod

class Services(ABC):
    """
    "Services" this represents basic function for business logic like
    request serialization and response deserialization before passed
    to the controller abstraction, generally other business logic
    that inherits this class will have function serialize, manipulator
    and deserialize.
    """

    @abstractmethod
    def serialize(self): pass

    @abstractmethod
    def manipulator(self): pass

    @abstractmethod
    def deserialize(self): pass