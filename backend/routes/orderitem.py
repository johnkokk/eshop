from datetime import datetime
from fastapi import APIRouter
from database.db import conn
from models.index import Order_Items
from schemas.index import Order_Item
from schemas.index import Error
from fastapi.responses import JSONResponse

orderitem = APIRouter()

@orderitem.get("/order_items")
async def read_data():
    return conn.execute(Order_Items.select()).fetchall()