from pydantic import BaseModel
from app.responses import ResponseBase
from components import services


class ServiceFoo(services.Services):
    def _validate(self):
        pass
        # raise ServicesLevelValidateException("validate", 403)

    def _logics(self) -> (BaseModel, int):
        self._validate()
        response_model = ResponseBase()
        response_model.response_code = "00"
        response_model.response_message = "Success"
        # raise ServicesLevelLogicsException("logics", 500)
        print("foo service executed")
        return response_model, 200

    def retrieve(self) -> (BaseModel, int):
        response_model, response_htt_code = self._logics()
        # raise ServicesLevelRetrieveException("retrieve", 404)
        return response_model, response_htt_code


class ServiceBar(services.Services):
    def _validate(self):
        pass
        # raise ServicesLevelValidateException("validate", 403)

    def _logics(self) -> (BaseModel, int):
        self._validate()
        response_model = ResponseBase()
        response_model.response_code = "00"
        response_model.response_message = "Success"
        # raise ServicesLevelLogicsException("logics", 403)
        print("bar service executed")
        return response_model, 200

    def retrieve(self) -> (BaseModel, int):
        response_model, response_htt_code = self._logics()
        # raise ServicesLevelRetrieveException("retrieve", 404)
        return response_model, response_htt_code
