from sqlmodel import SQLModel, Field

from models.user import User
from models.product import Product

class Cart(SQLModel, table=True):
  id: int = Field(primary_key=True)
  uuid: int = Field(min_length=16, max_length=16, index=True)
  user: User = Field(foreign_key=True)
  products: list[Product] | list[None] = Field(foreign_key=True)