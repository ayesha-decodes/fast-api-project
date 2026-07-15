from sqlmodel import SQLModel, create_engine
from urllib.parse import quote_plus

DATABASE_URL = (
    "mysql+pymysql://root:"
    + quote_plus("1234")
    + "@localhost:3306/employee"
)

engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)