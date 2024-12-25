from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# provavelmente chamado de schema no contexto 
class UserDTO(BaseModel):
  id: Optional[int] = Field(default=1, description="Id do usuário")
  name: str = Field(min_length=2, max_length=100, description="Nome do usuário.")
  email: EmailStr = Field(description="E-mail do usuário")
  is_active: bool = Field(default=True, description="Indica se o usuário está ativo")
  
  class Config:
    orm_mode = True