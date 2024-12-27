from sqlmodel import SQLModel, Field


class Foo(SQLModel):
	id: int | None = Field(default=None, primary_key=True)
	lines: list[str] = Field(min_length=6, max_length=12, index=True)


