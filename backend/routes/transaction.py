from datetime import datetime
from fastapi import APIRouter
from database.db import conn
from models.index import Transactions
from schemas.index import Transaction
from schemas.index import Error
from fastapi.responses import JSONResponse

transaction = APIRouter()

@transaction.get("/transactions")
async def read_data():
    return conn.execute(Transactions.select()).fetchall()

@transaction.get("/transaction/{transactionId}")
async def read_data(transactionId: int):

    exists = conn.execute(Transactions.select().where(Transactions.c.transaction_id == transactionId)).scalar()
    if(transactionId == exists):
        return conn.execute(Transactions.select().where(Transactions.c.transaction_id==transactionId)).fetchone()
    else:
        error=Error(code=404,reason="This transaction id does not exist")
        return JSONResponse(status_code=404, content={"code": error.code, "reason":error.reason}) 