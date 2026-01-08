from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:Anninha16!@localhost:3306/schema_connection")

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM users"))
    rows = result.fetchall()

print(rows)

