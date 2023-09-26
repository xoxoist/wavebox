from abc import ABC, abstractmethod
from definitions import Applications


class Routes(ABC):

    @abstractmethod
    def create_routes(self): raise NotImplemented

    @abstractmethod
    def apply(self) -> Applications: raise NotImplemented
