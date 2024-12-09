from fastapi import APIRouter, Header, WebSocket
from typing import Optional
from enums import food_type

router = APIRouter()

fruitsDictList: list[dict] = [
  {'type': food_type.FRUIT, 'name': 'orange'},
  {'type': food_type.FRUIT, 'name': 'apple'},
  {'type': food_type.FRUIT, 'name': 'pear'},
  {'type': food_type.FRUIT, 'name': 'banana'},
  {'type': food_type.FRUIT, 'name': 'kiwi'},
  {'type': food_type.FRUIT, 'name': 'apple'},
  {'type': food_type.FRUIT, 'name': 'banana'}
]

fruitsNameList: list[str] = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

router.get('/request_optional')
async def read_products_by_name_type(name: Optional[str], age: int):
  return

router.get("/products/fruits", tags=["fruits"])
async def read_products_fruits():
  return fruitsList

router.get("/products/{product_id}")
async def read_product_by_id(product_id: int):
  return{"product_id": product_id}

router.get("/")
def hello_api():
    return {"msg":"Hello FastAPI🚀"}
  
router.get('/get_headers')
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
  
  
  
  
  
# @app.get("/greet/{name}")
# async def greet_name(name:str) -> list:
#   return [""]


# router.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Message text was: {data}")