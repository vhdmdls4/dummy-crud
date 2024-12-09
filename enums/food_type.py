from enum import Enum

class FoodType(str, Enum):
  FRUITS = ("FRUITS")
  VEGETABLES = "VEGETABLES"
  DAIRY = "DAIRY"