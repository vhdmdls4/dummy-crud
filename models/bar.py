from typing import Optional

from sqlmodel import SQLModel, Field


class Bar(SQLModel, table=True):
	name: str = Field(index=True)
	age: Optional[int] = None