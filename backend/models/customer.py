from sqlalchemy import Table, Column, Integer, String, Float, Enum, Text
from database.db import meta


Customers = Table(

    'Customer', meta,
    Column('customer_id', Integer, primary_key=True),
    Column('first_name', String(30)),
    Column('last_name', String(50)),
    Column('email', String(100)),
    Column('address', String(200)),
    Column('city', String(100)),
    Column('telephone', Integer)
    
)