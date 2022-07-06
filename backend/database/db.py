from sqlalchemy import create_engine, MetaData

passkey = input("Enter passkey: ")
#engine = create_engine("mysql+pymysql://")
engine = create_engine(f"mysql+pymysql://db20_{passkey}:{passkey}@150.140.186.221:3306/al_db20_{passkey}")
meta=MetaData()
conn = engine.connect()

