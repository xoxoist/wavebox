#This is a generated service template
from typing import List
from flask import Blueprint
from pydantic import BaseModel
from data_model.response_model import ResponseBase
from wavebox.components.controllers import Controllers, EmptyBaseModel
from wavebox.components.exceptions import FundamentalException

from wavebox.components.services import Services
from wavebox.definitions.applications import Applications

class FooResponse(BaseModel):
    response_code: str | None = None
    response_message: str | None = None

class FooRequest(BaseModel):
    pass

class FooApiService(Services):
    
    def _validate(args):
        pass
    
    def _logics(self, req) -> (BaseModel, int):
        response_model = FooResponse()
        response_model.response_code = "200"
        response_model.response_message = "Get Foo Success"
        return response_model, 200

    def retrieve(self, req: BaseModel) -> (BaseModel, int):
        response_model, response_http_code = self._logics(req)
        return response_model, response_http_code
        
class FooApiController(Controllers, FooApiService):

    def __init__(self, blueprint: Blueprint, endpoint: str, methods: List[str]):
        FooApiService.__init__(self)
        super().__init__(blueprint, endpoint, methods)

    def controller(self):
        try:
            super().before(EmptyBaseModel)
            super().apply(*self.retrieve(None))
            super().after(FooResponse)
            return super().done()
        except FundamentalException as e:
            err_response = ResponseBase()
            err_response.response_code = e.error_code
            err_response.response_message = str(e)
            return super().catcher(err_response, e)
