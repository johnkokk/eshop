from pydantic import BaseModel

class Transaction(BaseModel):
    # transaction_id: int
    order_id: int
    amount: float
