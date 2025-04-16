import sqlite3

DB_FILE = "users.db"

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

def init_mapping_table():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product_role_map (
            product_name TEXT PRIMARY KEY,
            role_name TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_role_by_product(product_name: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT role_name FROM product_role_map WHERE product_name = ?", (product_name,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def add_product_role_mapping(product_name: str, role_name: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO product_role_map (product_name, role_name) VALUES (?, ?)", (product_name, role_name))
    conn.commit()
    conn.close()

def get_all_product_role_mappings():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT product_name, role_name FROM product_role_map")
    results = cursor.fetchall()
    conn.close()
    return results

def remove_product_role_mapping(product_name: str):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM product_role_map WHERE product_name = ?", (product_name,))
    deleted = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted > 0
