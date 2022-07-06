from datetime import datetime
from fastapi import APIRouter
from database.db import conn
from models.index import Orders
from schemas.index import Order
from schemas.index import Error
from fastapi.responses import JSONResponse

from models.index import Customers
from sqlalchemy import desc 

order = APIRouter()


@order.get("/orders")
async def read_data():
    return conn.execute(Orders.select()).fetchall()

@order.get("/order/{orderId}")
async def read_data(orderId: int):
    try:
        exists = conn.execute(Orders.select().where(Orders.c.order_id == orderId)).scalar()
        if(orderId == exists):
            return conn.execute(Orders.select().where(Orders.c.order_id==orderId)).fetchone()
        else:
            error=Error(code=404,reason="This order id does not exist")
            return JSONResponse(status_code=404, content={"code": error.code, "reason":error.reason})
    except Exception:
        error=Error(code=500, reason="Internal server error")
        return JSONResponse(status_code=500, content={"code": error.code, "reason":error.reason})

@order.get("/orderByCustomer/{customerId}")
async def read_data(customerId: str):
    return conn.execute(Orders.select().where(Orders.c.customer_id==customerId)).fetchall()


@order.post("/order")
async def write_data(Order: Order):

    exists = conn.execute(Customers.select().where(Customers.c.customer_id == Order.customer_id)).scalar()
    if(Order.customer_id != exists):
        error=Error(code=404,reason="This customer does not exist")
        return JSONResponse(status_code=404, content={"code": error.code, "reason":error.reason})

    try:
        conn.execute(Orders.insert().values(
            customer_id = Order.customer_id,
            date = Order.date
        ))
        return conn.execute(Orders.select().order_by(desc(Orders.c.order_id))).fetchone()

    except Exception:
            error=Error(code=500, reason="Internal server error")
            return JSONResponse(status_code=500, content={"code": error.code, "reason":error.reason})


@order.put("/order/{orderId}")
async def update_data(orderId: int, Order: Order):

    try:
        exists = conn.execute(Orders.select().where(Orders.c.order_id == orderId)).scalar()
        if(orderId == exists):
            
            exists = conn.execute(Customers.select().where(Customers.c.customer_id == Order.customer_id)).scalar()
            if(Order.customer_id != exists):
                error=Error(code=404,reason="This customer does not exist")
                return JSONResponse(status_code=404, content={"code": error.code, "reason":error.reason})
            
            conn.execute(Orders.update().values(
                customer_id = Order.customer_id,
                date = Order.date
            ).where(Orders.c.order_id==orderId))
            return conn.execute(Orders.select().where(Orders.c.order_id == orderId)).fetchone()
        
        else:
            error=Error(code=404,reason="This Order id does not exist")
            return JSONResponse(status_code=404, content={"code": error.code, "reason":error.reason})
    
    except Exception:
            error=Error(code=500, reason="Internal server error")
            return JSONResponse(status_code=500, content={"code": error.code, "reason":error.reason})

@order.delete("/order/{orderId}")
async def delete_data(orderId: int):

    try:
        exists = conn.execute(Orders.select().where(Orders.c.order_id == orderId)).scalar()
        if(orderId == exists):
            conn.execute(Orders.delete().where(Orders.c.order_id==orderId))
            # return conn.execute(Orders.select()).fetchall()
            return ("Order deleted successfully.")
        else:
            error=Error(code=404,reason="This Order does not exist")
            return JSONResponse(status_code=404, content={"code": error.code, "reason":error.reason})

    except Exception:
            error=Error(code=500, reason="Internal server error")
            return JSONResponse(status_code=500, content={"code": error.code, "reason":error.reason})