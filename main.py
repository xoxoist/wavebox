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

from pydantic import BaseModel
from flask import Flask, Blueprint, request, jsonify
from structure import group, controllers, services


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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = Flask(__name__)
    root = group.Group(__name__, "foo_or_bar_api", "/foobar/api/v1/")

    controller_foo = ControllerFoo(root, path="/foo")

    app.register_blueprint(controller_foo.blueprint)
    app.run(debug=True, port=5002)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
