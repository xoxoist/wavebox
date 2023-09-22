from structure.controllers import Controllers

class RoutesExtension:

    def __init__(self, routes: []):
        self.routes = routes

    def register_route(self, app):
        print("test" + str(self.routes))
        for route in self.routes:
            if isinstance(route, Controllers):
                app.register_blueprint(route.blueprint)