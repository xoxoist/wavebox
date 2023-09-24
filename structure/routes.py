from abc import ABC, abstractmethod
from structure.application import ApplicationService


class Routes(ABC):

    @abstractmethod
    def create_routes(self): raise NotImplemented

    @abstractmethod
    def apply(self) -> ApplicationService: raise NotImplemented
