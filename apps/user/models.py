import uuid

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

from config.database import db

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = sa.Column(sa.BigInteger, primary_key=True)
    email = sa.Column(sa.String(50), unique=True, nullable=False)
    password = sa.Column(sa.String(10), nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.now(), index=True)
    customer = relationship("Customer", back_populates="user", uselist=False)

class Customer(Base):
    __tablename__ = 'customer'

    id = sa.Column(sa.BigInteger, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("user.id"), unique=True)
    user = relationship("User", back_populates="customer")
    name = sa.Column(sa.String(50), nullable=False)
    birthday = sa.Column(sa.Date, nullable=False)
    account_number = sa.Column(sa.Integer, default=(uuid.uuid4().int & (1<<32)))
