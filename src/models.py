from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from config import Drinks, Stores


# Many-to-many association table
store_drink_association = Table(
    'store_drink', Base.metadata,
    Column('store_id', Integer, ForeignKey('Stores.id')),
    Column('drink_id', Integer, ForeignKey('Drinks.id'))
)


Base = declarative_base()

class Drink(Base):
    __tablename__ = 'Drinks'

    id = Drinks.Column(Drinks.Integer(), primary_key=True)
    name = Drinks.Column(Drinks.String(500), nullable=False, unique=True)
    normal_cost = Drinks.Column(Drinks.Float(), nullable=False)
    discount_cost = Drinks.Column(Drinks.Float(), nullable=False)
    image_url = Drinks.Column(Drinks.String(200))
    is_zero = Drinks.Column(Drinks.Boolean(), default=False)

    stores = relationship('Store', secondary=store_drink_association, back_populates='Drinks')


class Store(Base):
    __tablename__ = 'Stores'

    id = Stores.Column(Stores.Integer(), primary_key=True)
    name = Stores.Column(Stores.String(50), nullable=False, unique=True)
    logo_url = Stores.Column(Stores.String(200))

    drinks = relationship('Drink', secondary=store_drink_association, back_populates='Stores')

