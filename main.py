# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# class Registrar:
#     _app: Flask = Flask(__name__)
#     _debug: bool = True
#     _port: int = 5029
#
#     def listen(self):
#         self._app.run(debug=self._debug, port=self._port)

# external_data = {
#         'first_name': 'Isa',
#         'last_name': 'Wij',
#     }
#
#     try:
#         r = RequestCreateFoo(**external_data)
#         print(r.model_dump_json())
#     except ValidationError as e:
#         print(e.errors())

from flask import (Blueprint, Flask, make_response, request)
from pydantic import BaseModel
from structure.application import ApplicationService
from structure import group, controllers, services

def to_kebab_case(string: str) -> str:
    return ''.join(['-' + i.capitalize() if i.isupper() else i for i in string]).lstrip('-')

class HeaderBase(BaseModel):
    Authorization: str
    ContentType: str | None
    
    class Config:
        alias_generator = to_kebab_case

class ResponseBase(BaseModel):
    response_code: str | None = None
    response_message: str | None = None


class RequestCreateFoo(BaseModel):
    foo_first_name: str | None = None
    foo_last_name: str | None = None


class RequestCreateBar(BaseModel):
    foo_first_name: str
    foo_last_name: str


class ServiceFoo(services.Services):
    def _validate(self) -> bool:
        return True

    def _logics(self) -> (BaseModel, int):
        if self._validate():
            response_model = ResponseBase()
            response_model.response_code = "00"
            response_model.response_message = "validation error"
            return response_model, 500

        response_model = ResponseBase()
        response_model.response_code = "00"
        response_model.response_message = "Success"
        return response_model, 200

    def retrieve(self) -> (BaseModel, int):
        response_model, response_htt_code = self._logics()
        return response_model, response_htt_code


class ControllerFoo(controllers.Controllers, ServiceFoo):
    def __init__(self, blueprint: Blueprint, path: str):
        super().__init__(blueprint, path)

    def controller(self):
        super().before(RequestCreateFoo)

        response_model, response_http_code = self.retrieve()
        super().apply(response_model, response_http_code)

        super().after(ResponseBase)
        return super().done()

test_controller = ControllerFoo(group.Group(__name__, "test_blueprint", "/api/v1"), path="/foo")
application_service = ApplicationService()
application_service.add_controller(controller=test_controller)
app = application_service.create_app()

def main():
    app.run(debug= True, port=5002)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    app = Flask(__name__)

    root = Blueprint(__name__, "foo_or_bar_api", "/api/v1")

    @app.route("/foo")
    def fooFunc():
        # header_data = {
        #     'Authorization': "Bearer tesodfksdp2020202",
        #     'Content-Type': "application/json"
        # }

        # headersWithoutAuthorization = {
        #     'Content-Type': "application/json"
        # }

        err: str = None

        try:
            headers = HeaderBase(**request.headers)

            request.headers[headers]
        except Exception as e:
            print(e)
            err = str(e)

        

    app.register_blueprint(root)
    app.run(debug=True, port=5002)

    # main()

    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
