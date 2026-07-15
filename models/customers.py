from typing import Optional
from sqlmodel import SQLModel, Field


class customers(SQLModel, table=True):
    __tablename__ = "customers"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    mobile: str


class customers_update(SQLModel):
    name: Optional[str] = None
    email: Optional[str] = None
    mobile: Optional[str] = None