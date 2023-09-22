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
            super().middleware_after()
            return 'Route 2'
        except Exception as e:
            print(e)

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
