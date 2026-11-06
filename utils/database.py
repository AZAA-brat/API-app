import sqlite3
from contextlib import contextmanager
from utils.config import DB_PATH

@contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        yield conn
        conn.commit()
    finally:
        cursor.close()

def init_db():
    with get_db() as db:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            created_at NOT NULL
            );
            """
        )

init_db()