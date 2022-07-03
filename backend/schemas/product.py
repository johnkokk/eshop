from pydantic import BaseModel

class Product(BaseModel):
    name: str
    brand: str
    description: str
    price: float
    cost: float 
    stock: int
    size: str
    category: str