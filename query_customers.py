from sqlmodel import Session, select
from config.database import engine
from models.customers import customers

def all_customers(offset: int = 0, limit: int = 100):
    with Session(engine) as session:
        statement = select(customers).offset(offset).limit(limit)
        return session.exec(statement).all()
    
def customer_by_id(id: int):
    with Session(engine) as session:
        result = session.get(customers, id)
        return result