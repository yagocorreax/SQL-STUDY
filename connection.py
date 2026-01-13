from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:1234@localhost:3306/Filmes")

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM users"))
    rows = result.fetchall()

print(rows)

