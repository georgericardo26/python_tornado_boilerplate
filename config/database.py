from tornado_sqlalchemy import SQLAlchemy

from config.settings import DATABASES

db_default = DATABASES["default"]["DATABASE_URL"]
db = SQLAlchemy(db_default)
