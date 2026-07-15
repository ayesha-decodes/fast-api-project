from sqlmodel import Session
from config.database import engine
from models.customers import customers

def add_data(cust):
    with Session(engine) as session:
        session.add(cust)
        session.commit()
        session.refresh(cust)
        return cust
        