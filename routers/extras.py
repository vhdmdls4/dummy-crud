from http import HTTPStatus
from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse

from enums.food_type import FoodType
from models.generic_response import GenericResponse

router = APIRouter(prefix="/extras", tags=["extras"])

@router.get("/food_types/{food_type}")
async def read_food_type(food_type: FoodType):
  if food_type is FoodType.DAIRY_PRODUCTS: 
    return {"food_type": FoodType.DAIRY_PRODUCTS, "message": "Yummy... I like this dairy product a lot!!!"}
  if food_type == FoodType.FRUITS:
    return {"food_type": FoodType.FRUITS, "message": "Ok, fruits can be good too!"}
  return {"food_type": [food_type.value for food_type in FoodType]}
  
@router.get("/generic_response", response_model=GenericResponse[str])
async def read_generic_response():
  return GenericResponse[str](status=HTTPStatus.OK, message="Really good, using GenericResponse as usual!", data="Receiveee \\('o')/ (:brain)")

@router.get("/json_response")
async def read_json_response():
  return JSONResponse(content={"status": HTTPStatus.OK, "message": "Data fetched", "data": "Hello, World!"})

@router.get('/get_headers')
async def get_headers(
  accept:str = Header(None),
  content_type:str = Header(None),
  user_agent:str = Header(None),
  host:str = Header(None)
):
  request_headers = {}
  
  request_headers["Accept"] = accept
  request_headers["Content-Type"] = content_type
  request_headers["User-Agent"] = user_agent
  request_headers["Host"] = host