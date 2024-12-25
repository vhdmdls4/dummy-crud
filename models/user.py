from pydantic import EmailStr
from sqlmodel import Field, Session, SQLModel, create_engine, select
from enums.user_status import UserStatus


class User(SQLModel, table=True):
  id: int = Field(primary_key=True)
  name: str = Field(min_length=2, max_length=100, index=True)
  email: EmailStr = Field(index=True)
  is_active: bool = Field(default=True, index=True)
  user_status: UserStatus | None = Field(index=True)