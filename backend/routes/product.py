from fastapi import APIRouter
from database.db import conn
from models.index import Products
from schemas.index import Product



product = APIRouter()


@product.get("/")
async def read_data():
    return {"msg": "Hello"}

@product.get("/products")
async def read_data():
    return conn.execute(Products.select()).fetchall()

@product.get("/product/{id}")
async def read_data(id: int):
    return conn.execute(Products.select().where(Products.c.product_id==id))

@product.get("/productsByBrand/{brand}")
async def read_data(brand: str):
    return conn.execute(Products.select().where(Products.c.brand==brand)).fetchall()

@product.get("/productsByCategory/{category}")
async def read_data(category: str):
    return conn.execute(Products.select().where(Products.c.category==category)).fetchall()

@product.post("/")
async def write_data(Product: Product):

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
    return conn.execute(Products.select()).fetchall()

@product.put("/{id}")
async def update_data(id: int, Product: Product):
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
    return conn.execute(Products.select().where(Products.c.product_id==id))

@product.delete("/{id}")
async def delete_data(id: int):
    conn.execute(Products.delete().where(Products.c.product_id==id))
    return conn.execute(Products.select()).fetchall()