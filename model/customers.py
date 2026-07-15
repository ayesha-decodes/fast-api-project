from typing import Optional
from sqlmodel import SQLModel, Field
class customers(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str
    mobile: str

class customers_update(SQLModel):
    email: str
    mobile: Optional[str] = None