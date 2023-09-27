# library imports
from flask import Blueprint


class Routes(Blueprint):
    incoming_blueprint: Blueprint | None = None

    def __init__(self, name: str, import_name: str, url_prefix: str, blueprint: Blueprint | None = None):
        super().__init__(name, import_name, url_prefix=url_prefix)
        if blueprint is not None:
            self.incoming_blueprint = blueprint
            self.url_prefix = blueprint.url_prefix + url_prefix
            self.register_blueprint(blueprint)
        else:
            self.url_prefix = url_prefix

    def use(self, before, after):
        if self.incoming_blueprint is None:
            raise Exception("No Blueprint provide")
        else:
            self.incoming_blueprint.before_request(before)
            self.incoming_blueprint.after_request(after)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
