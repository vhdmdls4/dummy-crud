from http import HTTPStatus
from fastapi import FastAPI, Header
from fastapi.responses import JSONResponse

from enums.food_type import FoodType
from models.generic_response import GenericResponse

app = FastAPI()

# note: 
'''
Because path operations are evaluated in order, you need to make sure that the path for /users/me is declared before the one for /users/{user_id}
Otherwise, the path for /users/{user_id} would match also for /users/me, "thinking" that it's receiving a parameter user_id with a value of "me".
'''
@app.get("/")
async def root():
    return {"message": "Hello World"}
  
@app.get("/users/{user_id}")
async def read_user_by_id(user_id):
  return {"user_id": user_id}

@app.get("/users")
async def read_all_users():
  return ["Teste", "Outro teste", "Mais um teste"]

@app.get("/food_types/{food_type}")
async def read_food_type(food_type: FoodType):
  if food_type is FoodType.DAIRY_PRODUCTS: 
    return {"food_type": FoodType.DAIRY_PRODUCTS, "message": "Yummy... I like this dairy product a lot!!!"}
  if food_type == FoodType.FRUITS:
    return {"food_type": FoodType.FRUITS, "message": "Ok, fruits can be good too!"}
  return {"food_type": [food_type.value for food_type in FoodType]}
  
@app.get("/generic_response", response_model=GenericResponse[str])
async def read_generic_response():
  return GenericResponse[str](status=HTTPStatus.OK, message="Really good, using GenericResponse as usual!", data="Receiveee \\('o')/ (:brain)")

@app.get("/json_response")
async def read_json_response():
  return JSONResponse(content={"status": HTTPStatus.OK, "message": "Data fetched", "data": "Hello, World!"})

@app.get('/get_headers')
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