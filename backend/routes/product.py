from fastapi import APIRouter
from database.db import conn
from models.index import Products
from schemas.index import Product
from schemas.index import Error
from fastapi.responses import JSONResponse
from sqlalchemy import desc 

product = APIRouter()


@product.get("/products")
async def read_data():
    return conn.execute(Products.select()).fetchall()


@product.get("/product/{id}")
async def read_data(id: int):
    try:
        exists = conn.execute(Products.select().where(Products.c.product_id == id)).scalar()
        if(id == exists):
            return conn.execute(Products.select().where(Products.c.product_id==id)).fetchone()
        else:
            error=Error(code=404,reason="This product does not exist")
            return JSONResponse(status_code=404, content={"code": error.code, "reason":error.reason})
    
    except Exception:
        error=Error(code=500, reason="Internal server error")
        return JSONResponse(status_code=500, content={"code": error.code, "reason":error.reason})



@product.get("/productsByBrand/{brand}")
async def read_data(brand: str):
    return conn.execute(Products.select().where(Products.c.brand==brand)).fetchall()


@product.get("/productsByCategory/{category}")
async def read_data(category: str):
    return conn.execute(Products.select().where(Products.c.category==category)).fetchall()


@product.post("/product")
async def write_data(Product: Product):
    
    try:
        conn.execute(Products.insert().values(
            name= Product.name,
            brand= Product.brand,
            description= Product.description,
            price= Product.price,
            cost= Product.cost,
            stock= Product.stock,
            size= Product.size,
            category= Product.category
        ))
        return conn.execute(Products.select().order_by(desc(Products.c.product_id))).fetchone()
    
    except Exception:
        error=Error(code=500, reason="Internal server error")
        return JSONResponse(status_code=500, content={"code": error.code, "reason":error.reason})


@product.put("/product/{id}")
async def update_data(id: int, Product: Product):
    try:
        exists = conn.execute(Products.select().where(Products.c.product_id == id)).scalar()
        if(id == exists):
            conn.execute(Products.update().values(
                name= Product.name,
                brand= Product.brand,
                description= Product.description,
                price= Product.price,
                cost= Product.cost,
                stock= Product.stock,
                size= Product.size,
                category= Product.category
            ).where(Products.c.product_id==id))
            return conn.execute(Products.select().where(Products.c.product_id == id)).fetchone()
        else:
            error=Error(code=404,reason="This product does not exist")
            return JSONResponse(status_code=404, content={"code": error.code, "reason":error.reason})
    
    except Exception:
        error=Error(code=500, reason="Internal server error")
        return JSONResponse(status_code=500, content={"code": error.code, "reason":error.reason})
        

@product.delete("/product/{id}")
async def delete_data(id: int):
    
    try:
        exists = conn.execute(Products.select().where(Products.c.product_id == id)).scalar()
        if(id == exists):
            conn.execute(Products.delete().where(Products.c.product_id==id))
            #return conn.execute(Products.select()).fetchall()
            return "Product deleted successfully"
        else:
            error=Error(code=404,reason="This product does not exist")
            return JSONResponse(status_code=404, content={"code": error.code, "reason":error.reason})
    
    except Exception:
        error=Error(code=500, reason="Internal server error")
        return JSONResponse(status_code=500, content={"code": error.code, "reason":error.reason})