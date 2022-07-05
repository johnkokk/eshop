from pydantic import BaseModel

class Order_Item(BaseModel):
    order_id: int
    product_id: int
    quantity: int