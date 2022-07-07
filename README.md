# Sports e-shop
Simple api for a sports e-shop

## Dependencies (installation and running)
Before running install requirements
`pip install -r ./requirements.txt `

Also, a connection to UPatras' Network is required to connect to the database

Running the app from /eshop
`python3 backend/main.py`
The app is listening to port 8000

A passkey is requested for the database connection
Change settings on file backend/database/db.py

The app is Docker-ready

#Documentation
While the app, you can also find the docs @ http://localhost:8000/docs

## /product/{id} (GET)
Get a product by id (get method). Response will look like this:

```
{
  "product_id": integer,
  "name": "string",
  "brand": "string",
  "description": "string",
  "price": integer,
  "cost": integer,
  "stock": integer,
  "size": "string",
  "category": "string"
}
```
 
## /productsByBrand/{brand} (GET)
Get all products of a particular brand (get method). Response will look like this:

```
{
  "product_id": integer,
  "name": "string",
  "brand": "string",
  "description": "string",
  "price": integer,
  "cost": integer,
  "stock": integer,
  "size": "string",
  "category": "string"
}
```

## /productsByCategory/{category} (GET)
Get all products of a particular category (get method). Response will look like this:

```
{
  "product_id": integer,
  "name": "string",
  "brand": "string",
  "description": "string",
  "price": integer,
  "cost": integer,
  "stock": integer,
  "size": "string",
  "category": "string"
}
```

## /products (GET)
Get a list of all products (get method).

## /product (POST)
Insert a new product (post method). The new insertion will have to look like this:

```
{
  "name": "string",
  "brand": "string",
  "description": "string",
  "price": integer,
  "cost": integer,
  "stock": integer,
  "size": "string",
  "category": "string"
}
```

## /product/{id} (PUT)
Update/Edit an existing product (put method). The new insertion will have to look like this:

```
{
  "name": "string",
  "brand": "string",
  "description": "string",
  "price": integer,
  "cost": integer,
  "stock": integer,
  "size": "string",
  "category": "string"
}
```

## /product/{id} (DELETE)
Remove a product (delete method). If successful, response will look like this:

` "Product deleted successfully" `

## /customer/{id} (GET)
Get a customer by id (get method). Response will look like this:

```
{
  "customer_id": integer,
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "address": "string",
  "city": "string",
  "telephone": integer
}
```

## /customers (GET)
Get a list of all customers (get method)

## /customerByLastName/{lastname}
Get customers using their lastname (get method). Response will look like this:

```
{
  "customer_id": integer,
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "address": "string",
  "city": "string",
  "telephone": integer
}
```


## /customer (POST)
Insert a new customer (post method). The new insertion will have to look like this:

```
{
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "address": "string",
  "city": "string",
  "telephone": integer
}
```

## /customer/{id} (PUT)
Update/Edit an existing customer (put method). The new insertion will have to look like this:

```
{
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "address": "string",
  "city": "string",
  "telephone": integer
}
```

## /customer/{id} (DELETE)
Remove a customer (delete method). If successful, response will look like this:

` "Customer deleted successfully" `

## /order/{order id} (GET)
Get order by order id (get method). Response will look like this:
```
{
  "order_id": integer,
  "customer_id": integer,
  "date":	datetime
}
```

## /orderByCustomer/{customer id} (GET)
Get order by customer id (get method). Response will look like this:
```
{
  "order_id": integer,
  "customer_id": integer,
  "date":	datetime
}
```

## /orders (GET)
Get list of all orders (get method)

## /transaction/{id} (GET)
Get transaction by transaction id (get method). Response will look like this:
```
{
  "transaction_id": integer,
  "order_id": integer,
  "amount":	float
}
```

## /transactions (GET)
Get list of all transactions (get method)

## /totalRevenue (GET)
Get the amount of total revenue (get method). Response will have to look like this:

` Total revenue: float `

## /bestSellers (GET)
Get list of products and the amount sold in descending order (get method). Response will have to look like this:

```
[{
    "product_id": integer,
    "Total Sold": integer
  }]
```

## /stockAlert (GET)
Get list of products with 5 or less (5<=) items in our inventory in ascending order(get method). Response will have to look like this:
```
[{
    "product_id": integer,
    "cost": integer,
    "stock": integer
  }
```
