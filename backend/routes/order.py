from datetime import datetime
from fastapi import APIRouter
from database.db import conn
from models.index import Orders
from schemas.index import Order
from schemas.index import Error
from fastapi.responses import JSONResponse

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

@order.get("/OrderByCustomer/{customerId}")
async def read_data(customerId: str):
    return conn.execute(Orders.select().where(Orders.c.customer_id==customerId)).fetchall()


# @order.post("/Order")
# async def write_data(Order: Order):

# #error handling probably not actually working 

#     try:
#         conn.execute(Orders.insert().values(
#             customer_id = Order.customer_id,
#             date = datetime.now()
#         ))
#         return ("Successful order")

#     except Exception:
#             print (Exception)
#             error=Error(code=500, reason="Internal server error")
#             return JSONResponse(status_code=500, content={"code": error.code, "reason":error.reason})


# @Order.put("/Order/{id}")
# async def update_data(id: int, Order: Order):
#     exists = conn.execute(Orders.select().where(Orders.c.Order_id == id)).scalar()
#     if(id == exists):
#         conn.execute(Orders.update().values(
#             first_name = Order.first_name,
#             last_name = Order.last_name,
#             email = Order.email,
#             address = Order.address,
#             city = Order.city,
#             telephone = Order.telephone
#         ).where(Orders.c.Order_id==id))
#         return Order
#     else:
#         error=Error(code=404,reason="This Order id does not exist")
#         return JSONResponse(status_code=404, content={"code": error.code, "reason":error.reason})

# @Order.delete("/Order/{id}")
# async def delete_data(id: int):

#     exists = conn.execute(Orders.select().where(Orders.c.Order_id == id)).scalar()
#     if(id == exists):
#         conn.execute(Orders.delete().where(Orders.c.Order_id==id))
#         # return conn.execute(Orders.select()).fetchall()
#         return ("Order deleted successfully.")
#     else:
#         error=Error(code=404,reason="This Order does not exist")
#         return JSONResponse(status_code=404, content={"code": error.code, "reason":error.reason})