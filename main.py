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
from flask import Flask, Blueprint, request
from structure import group, controllers, services


class ResponseBase(BaseModel):
    response_code: str
    response_message: str
    detail: dict


class RequestCreateFoo(BaseModel):
    foo_first_name: str
    foo_last_name: str


class RequestCreateBar(BaseModel):
    foo_first_name: str
    foo_last_name: str


class ServiceFoo(services.Services):
    def serialize(self):
        print("Serializing data from request")

    def manipulator(self):
        self.serialize()
        print("Executing service logics")

    def deserialize(self):
        self.manipulator()
        print("Deserialize data from manipulator")


class ControllerFoo(controllers.Controllers, ServiceFoo):
    def __init__(self, blueprint: Blueprint, path: str):
        super().__init__(request, blueprint, path)
        self.blueprint.add_url_rule(path, view_func=self.controller)

    def service(self):
        self.deserialize()

    def controller(self):
        try:
            super().header_validation()
            super().request_validation()
            super().middleware_before()
            self.service()
            super().middleware_before()
            return 'Route 2'
        except Exception as e:
            print(e)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = Flask(__name__)
    root = group.Group(__name__, "foo_or_bar_api", "/foobar/api/v1/")

    controller_foo = ControllerFoo(root, path="/foo")

    app.register_blueprint(controller_foo.blueprint)
    app.run(debug=True, port=5002)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
