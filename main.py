from flask import jsonify
from werkzeug.exceptions import HTTPException
from structure.application import ApplicationService
from app.routers.routers import RoutesFoo, RoutesBar
from app.responses import ResponseBase


def main():
    application_service = ApplicationService()
    application_service = RoutesFoo(application_service).apply()
    application_service = RoutesBar(application_service).apply()
    application_service.set_config(debug=1)
    app = application_service.create_app()

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
