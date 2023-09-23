from abc import ABC, abstractmethod


class Routes(ABC):

    @abstractmethod
    def register_route(self): raise NotImplemented
