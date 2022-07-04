from pydantic import BaseModel

class Error(BaseModel):
    code: int
    reason: str