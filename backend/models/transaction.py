from sqlalchemy import Table, Column, Integer, Float, ForeignKey
from database.db import meta


Transactions = Table(

    'Transaction', meta,
    Column('transaction_id', Integer, primary_key=True),
    Column('order_id', Integer, ForeignKey("Order.c.order_id")),
    Column('amount', Float)
)
