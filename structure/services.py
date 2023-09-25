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
    def _validate(self):
        """
        '_validate' this abstract method represents pre-defined method for validating incoming
        data from request you are freely defines this method behavior for support your business
        logic need before the data enters your business logic. tips: you can directly raise a
        class exception, if there is an error.
        """
        raise NotImplemented

    @abstractmethod
    def _logics(self) -> (BaseModel, int):
        """
        '_logics' this abstract method represents your business logic activity, your business
        logic process should be defined inside this method, you can do database queries, api
        calls, or some other calculation in order to make your business process run as you
        expected. tips: you can directly raise a class exception, if there is an error.
        :return: BaseModel, int
        """
        raise NotImplemented

    @abstractmethod
    def retrieve(self) -> (BaseModel, int):
        """
        'retrieve' this abstract method represent an entry to your business logic activity, you
        can post-defined after your business logic activity already executed and in this method
        you need to call '_logics' to receive its responses and this method will directly call
        from controller class. tips: you can directly raise a class exception, if there is an error.
        :return: BaseModel, int
        """
        raise NotImplemented
