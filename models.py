
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from db import db
from sqlalchemy.orm import relationship

class Customer(db):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(20), nullable=True)
    rented_books = relationship('RentedBook', back_populates='customer', cascade='all, delete-orphan')


class RentedBook(db):
    __tablename__ = 'rented_books'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False) 
    rent_date = Column(Date, nullable=False)  
    return_date = Column(Date, nullable=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)  
    customer = relationship('Customer', back_populates='rented_books')
