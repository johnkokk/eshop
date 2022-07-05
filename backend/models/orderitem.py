from sqlalchemy import Table, Column, Integer, String, Float, Enum, Text, DateTime, ForeignKey
from database.db import meta


Order_Items = Table(

    'Order_Item', meta,
    Column('order_id', Integer, primary_key=True),
    Column('product_id', Integer, primary_key=True),
    Column('quantity', Integer )
)

# ???? PrimKey ??