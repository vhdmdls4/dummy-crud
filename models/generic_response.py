from http import HTTPStatus
from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar('T')

class GenericResponse(BaseModel, Generic[T]): 
  status: HTTPStatus
  message: str
  data: T