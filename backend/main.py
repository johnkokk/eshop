from fastapi import FastAPI
from routes.index import product

app= FastAPI()

app.include_router(product)