import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            discord_id TEXT PRIMARY KEY,
            email TEXT UNIQUE
        )
    """)
    conn.commit()
    conn.close()

def link_user(discord_id: str, email: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO users (discord_id, email) VALUES (?, ?)", (discord_id, email))
    conn.commit()
    conn.close()

def get_discord_id_by_email(email: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT discord_id FROM users WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None
