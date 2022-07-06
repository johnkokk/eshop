import uvicorn
from fastapi import FastAPI
from routes.index import product
from routes.index import customer
from routes.index import order
from routes.index import orderitem
from routes.index import transaction

app= FastAPI()


@app.get("/")
async def read_data():
    return {"msg": "Hello! Welcome to our eshop."}

app.include_router(product)
app.include_router(customer)
app.include_router(order)
app.include_router(orderitem)
app.include_router(transaction)

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)