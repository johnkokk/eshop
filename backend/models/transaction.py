from sqlalchemy import Table, Column, Integer, String, Float, Enum, Text, DateTime, ForeignKey
from database.db import meta


Transactions = Table(

    'Transaction', meta,
    Column('transaction_id', Integer, primary_key=True),
    Column('order_id', Integer),
    Column('amount', Float)
)
