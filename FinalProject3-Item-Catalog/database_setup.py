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

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    image_name = Column(String(250))
    category_name = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user_name = Column(String(250), nullable=False)
    user = relationship(Users)


class SearchIndex(Base):
    __tablename__ = 'search_index'
    __table_args__ = {'prefixes': ['TEMPORARY']}

    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    name = Column(String(80), nullable=False)





engine = create_engine('sqlite:///salesite.db', echo=True)

Base.metadata.create_all(engine)
