
from db import SessionLocal
from models import Customer, RentedBook
from datetime import date

def insert_data():
    db = SessionLocal()

    customer = Customer(name="Alice Smith", email="alice@example.com", phone="123-456-7890")
    db.add(customer)
    db.commit()
    db.refresh(customer)

    rented_book = RentedBook(title="The Catcher in the Rye", rent_date=date.today(), customer_id=customer.id)
    db.add(rented_book)
    db.commit()
    db.refresh(rented_book)

    db.close()
    print(f"Customer and book inserted: {customer.name}, {rented_book.title}")

insert_data()

def update_customer_email(customer_id, new_email):
    db = SessionLocal()
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        customer.email = new_email
        db.commit()
    db.close()
    print(f"Customer email updated to {new_email}")

update_customer_email(1, "newalice@example.com")

def get_all_customers():
    db = SessionLocal()
    customers = db.query(Customer).all()
    db.close()
    return customers

print(get_all_customers())

def delete_customer(customer_id):
    db = SessionLocal()
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        db.delete(customer)
        db.commit()
    db.close()
    print(f"Customer with ID {customer_id} deleted")

delete_customer(1)

def delete_customer_with_rented_books(customer_id):
    db = SessionLocal()
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        db.delete(customer)
        db.commit()
    db.close()
    print(f"Customer with ID {customer_id} and all rented books deleted")

delete_customer_with_rented_books(2)