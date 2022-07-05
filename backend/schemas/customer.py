from pydantic import BaseModel

class Customer(BaseModel):
    first_name: str
    last_name: str
    email: str
    address: str
    city: str 
    telephone: int