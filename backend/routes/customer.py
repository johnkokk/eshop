from fastapi import APIRouter
from database.db import conn
from models.index import Customers
from schemas.index import Customer
from schemas.index import Error
from fastapi.responses import JSONResponse
from sqlalchemy import desc
import sqlalchemy as db

customer = APIRouter()


@customer.get("/customers")
async def read_data():
    return conn.execute(Customers.select()).fetchall()

@customer.get("/customer/{id}")
async def read_data(id: int):
    try:
        exists = conn.execute(Customers.select().where(Customers.c.customer_id == id)).scalar()
        if(id == exists):
            return conn.execute(Customers.select().where(Customers.c.customer_id==id)).fetchone()
        else:
            error=Error(code=404,reason="This customer id does not exist")
            return JSONResponse(status_code=404, content={"code": error.code, "reason":error.reason})
    
    except Exception:
        error=Error(code=500, reason="Internal server error")
        return JSONResponse(status_code=500, content={"code": error.code, "reason":error.reason})


@customer.get("/customersByLastName/{lastname}")
async def read_data(lastname: str):

    return conn.execute(Customers.select().where(Customers.c.last_name==lastname)).fetchall()

@customer.post("/customer")
async def write_data(Customer: Customer):
    
    try:
        exists = conn.execute(db.select([Customers.c.email])).fetchall()
        for i in range(0, len(exists)):
            if(Customer.email == exists[i][0]):
                error=Error(code=409, reason="This email already exists")
                return JSONResponse(status_code=409, content={"code": error.code, "reason":error.reason})
    
        conn.execute(Customers.insert().values(
            first_name = Customer.first_name,
            last_name = Customer.last_name,
            email = Customer.email,
            address = Customer.address,
            city = Customer.city,
            telephone = Customer.telephone
        ))
        return conn.execute(Customers.select().order_by(desc(Customers.c.customer_id))).fetchone()

    except Exception:
        error=Error(code=500, reason="Internal server error")
        return JSONResponse(status_code=500, content={"code": error.code, "reason":error.reason})


@customer.put("/customer/{id}")
async def update_data(id: int, Customer: Customer):
    
    try:
        exists = conn.execute(Customers.select().where(Customers.c.customer_id == id)).scalar()
        if(id == exists):
            conn.execute(Customers.update().values(
                first_name = Customer.first_name,
                last_name = Customer.last_name,
                email = Customer.email,
                address = Customer.address,
                city = Customer.city,
                telephone = Customer.telephone
            ).where(Customers.c.customer_id==id))
            return conn.execute(Customers.select().order_by(desc(Customers.c.customer_id))).fetchone()
        else:
            error=Error(code=404,reason="This customer id does not exist")
            return JSONResponse(status_code=404, content={"code": error.code, "reason":error.reason})
    
    except Exception:
        error=Error(code=500, reason="Internal server error")
        return JSONResponse(status_code=500, content={"code": error.code, "reason":error.reason})

@customer.delete("/customer/{id}")
async def delete_data(id: int):
    try:
        exists = conn.execute(Customers.select().where(Customers.c.customer_id == id)).scalar()
        if(id == exists):
            conn.execute(Customers.delete().where(Customers.c.customer_id==id))
            # return conn.execute(Customers.select()).fetchall()
            return ("Customer deleted successfully.")
        else:
            error=Error(code=404,reason="This customer id does not exist")
            return JSONResponse(status_code=404, content={"code": error.code, "reason":error.reason})
    except Exception:
        error=Error(code=500, reason="Internal server error")
        return JSONResponse(status_code=500, content={"code": error.code, "reason":error.reason})