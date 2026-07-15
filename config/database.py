from sqlmodel import SQLModel, create_engine
from urllib.parse import quote_plus
#Mysql connection string
engine=create_engine("mysql+pymysql://root:" + quote_plus("1234") + "@localhost:3306/fastapi", echo=True)

#function to create db tables from SQLModel classes
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)