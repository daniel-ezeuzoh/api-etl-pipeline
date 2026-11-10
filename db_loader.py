import sqlite3
from models import User

def save_users_to_db(users: list[User], db_name: str) -> None:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            city TEXT
        )
    """)

    for user in users:
        cursor.execute("""
            INSERT OR REPLACE INTO users (id, name, email, city)
            VALUES (?, ?, ?, ?)
        """, (user.user_id, user.name, user.email, user.city))

    conn.commit()
    conn.close()
    print("Database updated successfully!")