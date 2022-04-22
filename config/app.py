import tornado
from tornado_sqlalchemy import SQLAlchemy

from apps.user.handlers import UserHandler
from config.database import db

URLS = (
    (r"/", UserHandler),
)


def make_app():
    return tornado.web.Application(URLS, db=db)