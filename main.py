from fastapi import FastAPI, HTTPException, Query
from models.customers import customers, customers_update
from config.database import create_db_and_tables
from contextlib import asynccontextmanager
from add_customers import add_data
from query_customers import all_customers, customer_by_id
from update_customers import update_customer
from delete_customers import delete_customer

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app= FastAPI(lifespan=lifespan)

@app.get("/customers/",response_model=list[customers])
def customer_all(offset: int = 0, limit: int = Query(default=100, le=100)):
    result=all_customers(offset, limit)
    return result

# @app.get("/customers/", response_model=list[customers])
# def allcustomers():
#     result=all_customers()
#     return result

@app.post("/customers/", response_model=customers)
def add_customers(customer: customers):
    result=add_data(customer)
    return result

@app.get("/customers/{id}", response_model=customers)  
def get_customer_by_id(id: int):
    result=customer_by_id(id)
    print(result)
    if not result:
        raise HTTPException(status_code=404, detail="Customer not found")
    return result

@app.patch("/customers/{id}", response_model=customers)
def update(id: int, customer: customers_update):
    result=update_customer(id, customer)
    if not result:
        raise HTTPException(status_code=404, detail="Customer not found")
    return result

@app.delete("/customers/{id}")
def delete(id: int):
    result=delete_customer(id)
    if result==0:
        raise HTTPException(status_code=404, detail="Customer not found")
    else:
        return {"ok":True}