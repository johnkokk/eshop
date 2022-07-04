from fastapi import FastAPI
from routes.index import product

app= FastAPI()


@app.get("/")
async def read_data():
    return {"msg": "Hello! Welcome to our eshop."}

app.include_router(product)