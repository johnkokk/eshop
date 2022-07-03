from sqlalchemy import Table, Column, Integer, String, Float, Enum, Text
from database.db import meta


Products = Table(

    'Product', meta,
    Column('product_id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('brand', String(100)),
    Column('description', Text),
    Column('price', Float),
    Column('cost', Float),
    Column('stock', Integer),
    Column('size', String(10)),
    Column ('category', Enum('Shoes', 'Hats', 'T-Shirts', 'Shorts', 'Equipment'))
)