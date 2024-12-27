from sqlmodel import SQLModel, Field

from models.user import User

class Product(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    user: User = Field(foreign_key=True)
