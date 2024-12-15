from http import HTTPStatus
from fastapi import APIRouter, Depends

from dto.user_dto import UserDTO
from models.generic_response import GenericResponse

router = APIRouter(prefix="/users", tags=["users"])

# note: 
'''
Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}
Otherwise, the path for /users/{user_id} would match also for /users/me, "thinking" that it's receiving a parameter user_id with a value of "me".
'''


@router.get("/users/{user_id}")
async def read_user_by_id(user_id):
  return {"user_id": user_id}

@router.get("/users")
async def read_all_users():
  return ["Teste", "Outro teste", "Mais um teste"]

@router.post("/user")
async def create_user(userDTO: UserDTO):
  return GenericResponse[UserDTO](status=HTTPStatus.OK, message="User was created successfully", data=userDTO.model_dump())
  