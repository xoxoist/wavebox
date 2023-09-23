from flask import Request
from structure.middlewares import Middlewares


class FooMiddleware(Middlewares):
    def __init__(self, req: Request):
        super().__init__(req)
    
    def before(self):
        print("Middleware before", self.req.headers.get("Postman-Token"))
    
    def after(self):
        print("Middleware after", self.req.headers.get("Postman-Token"))