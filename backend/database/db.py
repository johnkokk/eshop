from sqlalchemy import create_engine, MetaData

# passkey = input("Enter passkey: ")
engine = create_engine("mysql+pymysql://")
meta=MetaData()
conn = engine.connect()

