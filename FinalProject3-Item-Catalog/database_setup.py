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


class UserDetails(Base):
    __tablename__ = 'userdetails'

    handle = Column(String(80), nullable=False)
    email = Column(String(250), primary_key=True)


class SaleItem(Base):
    __tablename__ = 'sale_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    category_id = Column(Integer, ForeignKey('category.id'))
    seller_id = Column(Integer, ForeignKey('users.id'))
    seller = relationship(Users)


class Category(Base):
    __tablename__ = 'category'

    name = Column(String(80), nullable=False)
    id = Column(Integer, pimary_key=True)
    description = Column(String(250))


engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
