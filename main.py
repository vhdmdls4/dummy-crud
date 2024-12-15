from http import HTTPStatus
from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse

from enums.food_type import FoodType
from models.generic_response import GenericResponse
from dto.user_dto import UserDTO
from routers import extras, user

app = FastAPI()

app.include_router(user.router)
app.include_router(extras.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}