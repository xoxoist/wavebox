# library imports
from abc import ABC, abstractmethod
from flask import Blueprint, Response, Request


# TODO : create interceptor class that will represent as middleware logics,
#  because in flask middleware focuses to global usage not for specific
#  still can be per-blueprint

class Middlewares(ABC):
    """
    'Middlewares' this represents class definition of your middleware basically this
    before and after function will be executed after your 'Services' logics function
    has been called you can access incoming request data by request attribute, and
    for response data you can catch it inside after function.
    """

    def __init__(self, path: str, req: Request | None):
        self.path = path
        self.request = req

    def set_blueprint(self, blueprint: Blueprint):
        """
        'set_blueprint' this function is protected to this abstract class that will be
        executed inside controller to initiate registration of your 'before' and 'after'
        middleware function, so your middleware will detect before and after procedure
        for business logic invocation.
        """
        blueprint.before_request(self.before)
        blueprint.after_request(self.after)

    @abstractmethod
    def before(self):
        """
        'before' this function represents middleware that will be executed before your logics,
        so you can raise an exception inside this function to halt the process execution of
        your business logics.
        """
        raise NotImplemented

    @abstractmethod
    def after(self, response: Response) -> Response:
        """
        'after' this function represents middleware that will be executed after your logics,
        so you can raise an exception inside this function to halt the returning process from
        your business logics, and validate what is needed to satisfy the middleware.
        :return: Response
        """
        raise NotImplemented
