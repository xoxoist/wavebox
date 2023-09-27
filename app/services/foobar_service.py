from pydantic import BaseModel
from app.models.responses import ResponseBase
from components import Services


class ServiceFoo(Services):
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


class ServiceBar(Services):
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
