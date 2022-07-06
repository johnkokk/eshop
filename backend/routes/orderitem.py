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

@orderitem.get("/bestSellers")
async def read_data():
    try:
        #query = db.select(db.func.sum(Order_Items.c.quantity).label("Total Sold")).group_by(Order_Items.c.product_id).order_by(desc("Total Sold"))
        query = 'SELECT product_id, sum(`Order_item`.quantity) AS `Total Sold` FROM `Order_item` GROUP BY product_id ORDER BY `Total Sold` DESC'
        best = conn.execute(query).fetchall()
        return best
    
    except Exception:
        error=Error(code=500, reason="Internal server error")
        return JSONResponse(status_code=500, content={"code": error.code, "reason":error.reason})