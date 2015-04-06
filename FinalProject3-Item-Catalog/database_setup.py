import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Sellers(Base):
    __tablename__ = 'sellers'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class SaleItem(Base):
    __tablename__ = 'sale_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    category_id = Column(Integer, ForeignKey('category.id'))
    seller_id = Column(Integer, ForeignKey('sellers.id'))
    seller = relationship(Sellers)


class Category(Base):
    __tablename__ = 'category'

    name = Column(String(80), nullable=False)
    id = Column(Integer, pimary_key=True)
    description = Column(String(250))




    # We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }


engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)
