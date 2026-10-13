from sqlalchemy import text

from database import engine

def test_conn():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("Connection successful", result.scalar())

if __name__ == "__main__":
    test_conn()  