from sqlalchemy import Table, Column, Integer, String, Float, Enum, Text, DateTime, ForeignKey
from database.db import meta


Orders = Table(

    'Order', meta,
    Column('order_id', Integer, primary_key=True),
    Column('customer_id', Integer),
    Column('date', DateTime )
)

# ?????????????????????????

