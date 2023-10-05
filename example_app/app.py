from flask import Blueprint, Flask, Response, jsonify
from pydantic import BaseModel
from werkzeug.exceptions import NotFound, BadRequest
from data_model.response_model import ResponseBase
from routes import ApplicationRouting
from wavebox.components.exceptions import FundamentalException
from wavebox.definitions.applications import Applications

class ExampleApp(Applications):
    def __init__(self, flask_app: Flask):
        super().__init__(flask_app, Blueprint('root', flask_app.name, url_prefix="/"))

    def provide_config(self):
        return super().provide_config()
        
    def global_handle_http_exception(self, ex: FundamentalException) -> Response:
        response = ResponseBase()

        if isinstance(ex, NotFound):
            response.response_code = "RNF404"
        elif isinstance(ex, BadRequest):
            response.response_code  = "BDR403"
        else:
            response.response_code = ex.code

        response.response_message = str(ex)
        response_data = jsonify(dict(response))
        response_data.status_code = ex.code
        return response_data

def main():
    app = Flask(__name__)
    example_app = ExampleApp(app)
    ApplicationRouting(example_app)
    example_app.start()

if __name__ == '__main__':
    main()