from sqlalchemy import Table, Column, Integer,ForeignKey
from database.db import meta


Order_Items = Table(

    'Order_item', meta,
    Column('order_id', Integer, ForeignKey("Order.c.order_id"), primary_key=True),
    Column('product_id', Integer, ForeignKey("Product.c.product_id"), primary_key=True),
    Column('quantity', Integer)
)