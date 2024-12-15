from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class UserDTO(BaseModel):
  id: Optional[int] = Field(None, "Id do usuário")
  name: str = Field(..., min_length=2, max_length=100, description="Nome do usuário.")
  