from fastapi import APIRouter

router = APIRouter()

@router.get("/products/fruits", tags=["fruits"])
async def read_products_fruits():
  return ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
