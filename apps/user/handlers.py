from tornado.web import RequestHandler
from tornado_sqlalchemy import SessionMixin

class UserHandler(SessionMixin, RequestHandler):
    def get(self):
        self.write("Hello, world 2")