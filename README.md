# Sports e-shop
Simple api for a sports e-shop

## Dependencies


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
  "order_id": integer
  "customer_id": integer
  "date":	datetime
 }
```

## /order/{customer id} (GET)
Get order by customer id (get method). Response will look like this:
```
{
  "order_id": integer
  "customer_id": integer
  "date":	datetime
 }
```

## /orders (GET)
Get list of all orders (get method)

## /transaction/{id} (GET)
Get transaction by transaction id (get method). Response will look like this:
```
{
  "transaction_id": integer
  "order_id": integer
  "amount":	float
 }
```

## /transactions (GET)
Get list of all transactions (get method)

## /transactions/totalRevenue (GET)
Get the amount of total revenue (get method). Response will have to look like this:

` Total revenue: float `
