from fastapi import APIRouter
from database.db import conn
from models.index import Customers
from schemas.index import Customer



customer = APIRouter()


@customer.get("/")
async def read_data():
    return {"msg": "Hello"}

@customer.get("/customers")
async def read_data():
    return conn.execute(Customers.select()).fetchall()

@customer.get("/customer/{id}")
async def read_data(id: int):
    return conn.execute(Customers.select().where(Customers.c.customer_id==id)).fetchall()

@customer.get("/CustomersByLastName/{lastname}")
async def read_data(lastname: str):
    return conn.execute(Customers.select().where(Customers.c.last_name==lastname)).fetchall()

# @customer.post("/")
# async def write_data(Customer: Customer):

#     conn.execute(Customers.insert().values(
#         name= Customer.name,
#         brand= Customer.brand,
#         description= Customer.description,
#         price= Customer.price,
#         cost= Customer.cost,
#         stock= Customer.stock,
#         size= Customer.size,
#         category= Customer.category
#     ))
#     return conn.execute(Customers.select()).fetchall()
#     # return conn.execute(Customers.select().where(Customers.c.Customer_id==max(id)).fetchall()
#     # return conn.execute(Customers.select()).fetchone()

# @Customer.put("/{id}")
# async def update_data(id: int, Customer: Customer):
#     conn.execute(Customers.update().values(
#         name= Customer.name,
#         brand= Customer.brand,
#         description= Customer.description,
#         price= Customer.price,
#         cost= Customer.cost,
#         stock= Customer.stock,
#         size= Customer.size,
#         category= Customer.category
#     ).where(Customers.c.Customer_id==id))
#     return conn.execute(Customers.select().where(Customers.c.Customer_id==id)).fetchall()

# @Customer.delete("/{id}")
# async def delete_data(id: int):
#     conn.execute(Customers.delete().where(Customers.c.Customer_id==id))
#     return conn.execute(Customers.select()).fetchall()