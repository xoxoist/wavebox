from flask import Blueprint, Response, Request, abort, jsonify
from pydantic import BaseModel
from werkzeug.exceptions import HTTPException
from structure.application import ApplicationService
from structure import groups, controllers, services, routes, middlewares
from structure.tools.request_header import HeaderBase
from troubles.exceptions import FundamentalException, ServicesLevelLogicsException, MiddlewaresLevelBeforeException


class ResponseBase(BaseModel):
    response_code: str | None = None
    response_message: str | None = None


class RequestCreateFoo(BaseModel):
    foo_first_name: str
    foo_last_name: str


class RequestCreateBar(BaseModel):
    bar_first_name: str
    bar_last_name: str


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


class FooMiddleware(middlewares.Middlewares):
    def __init__(self, req: Request | None):
        super(FooMiddleware, self).__init__(req)
        self.request = req

    def before(self):
        print("FOO MIDDLEWARE BEFORE", self.request.headers)
        # raise MiddlewaresLevelBeforeException("memeg", 503)
        # abort(401)

    def after(self, response: Response) -> Response:
        print("FOO MIDDLEWARE AFTER", response)
        # response.headers['Content-Type'] = 'application/json'
        # response.headers['Memeg'] = 'Memeg'
        # abort(401)
        return response


class BarMiddleware(middlewares.Middlewares):
    def __init__(self, req: Request | None):
        super(BarMiddleware, self).__init__(req)
        self.request = req

    def before(self):
        print("BAR MIDDLEWARE BEFORE", self.request.headers)
        raise MiddlewaresLevelBeforeException("memeg", 503)
        # abort(401)

    def after(self, response: Response) -> Response:
        print("BAR MIDDLEWARE AFTER", response)
        # response.headers['Content-Type'] = 'application/json'
        # response.headers['Memeg'] = 'Memeg'
        # abort(401)
        return response


class ControllerFoo(controllers.Controllers, ServiceFoo):
    def __init__(self, blueprint: Blueprint, path: str, endpoint: str):
        super().__init__(blueprint, path, endpoint, FooMiddleware)

    def controller(self):
        try:
            super().before(RequestCreateFoo, HeaderBase)
            super().apply(*self.retrieve())
            super().after(ResponseBase)
            return super().done()
        except FundamentalException as e:
            err_response = ResponseBase()
            err_response.response_code = "99"
            err_response.response_message = str(e)
            print(e.exception_tag)
            return super().catcher(err_response, e)


class ControllerBar(controllers.Controllers, ServiceBar):
    def __init__(self, blueprint: Blueprint, path: str, endpoint: str):
        super().__init__(blueprint, path, endpoint, BarMiddleware)

    def controller(self):
        try:
            super().before(RequestCreateBar, HeaderBase)
            super().apply(*self.retrieve())
            super().after(ResponseBase)
            return super().done()
        except FundamentalException as e:
            err_response = ResponseBase()
            err_response.response_code = "99"
            err_response.response_message = str(e)
            print(e.exception_tag)
            return super().catcher(err_response, e)


class RoutesBar(routes.Routes):

    def __init__(self, application_service: ApplicationService):
        self.application_service = application_service

    def create_routes(self):
        root = "/foobar/api/v1"
        self.application_service.add_controller(
            ControllerBar(groups.Groups(__name__, "test_blueprint", root),
                          path="/bar", endpoint="bar_endpoint"))

    def apply(self) -> ApplicationService:
        self.create_routes()
        return self.application_service


class RoutesFoo(routes.Routes):
    def __init__(self, application_service: ApplicationService):
        self.application_service = application_service

    def create_routes(self):
        root = "/foobar/api/v1"
        self.application_service.add_controller(
            ControllerFoo(groups.Groups(__name__, "test_blueprint", root),
                          path="/foo", endpoint="foo_endpoint"))

    def apply(self) -> ApplicationService:
        self.create_routes()
        return self.application_service


def main():
    application_service = ApplicationService()
    application_service = RoutesFoo(application_service).apply()
    application_service = RoutesBar(application_service).apply()

    app = application_service.create_app()

    # attributes = vars(ResponseBase)
    # for attribute, value in attributes.items():
    #     print(f"{attribute}: {value}")
    # print(dict(ResponseBase.__annotations__)["response_code"])

    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        response = ResponseBase()
        response.response_code = "99"
        response.response_message = str(e)
        response_data = jsonify(dict(response))
        response_data.status_code = e.code
        return response_data

    app.run(debug=True, port=5002)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

    # app = Flask(__name__)
    #
    # root = Blueprint(__name__, "foo_or_bar_api", "/api/v1")
    #
    #
    # @app.route("/foo")
    # def fooFunc():
    #     # header_data = {
    #     #     'Authorization': "Bearer tesodfksdp2020202",
    #     #     'Content-Type': "application/json"
    #     # }
    #
    #     # headersWithoutAuthorization = {
    #     #     'Content-Type': "application/json"
    #     # }
    #
    #     err: str = None
    #
    #     try:
    #         headers = HeaderBase(**request.headers)
    #
    #         request.headers[headers]
    #     except Exception as e:
    #         print(e)
    #         err = str(e)
    #
    #
    # app.register_blueprint(root)
    # app.run(debug=True, port=5002)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
