import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    social_id = Column(String(64), nullable=False, unique=True)


class SaleItem(Base):
    __tablename__ = 'sale_item'
    __searchable__ = ['description']
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(String(250))
    price = Column(String(8))
    image_name = Column(String(250))
    category_name = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user_name = Column(String(250), nullable=False)
    user = relationship(Users)

    def __init__(self, name, description, price, image_name, category_name, user_id, user_name):
        self.name = name
        self.description = description
        self.price = price
        self.image_name = image_name
        self.category_name = category_name
        self.user_id = user_id
        self.user_name = user_name

    def __repr__(self):
        return '<sale_item %d>' % self.id

engine = create_engine('sqlite:///salesite.db', echo=True)

Base.metadata.create_all(engine)
