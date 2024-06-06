import sqlite3

def create_database():
    conn = sqlite3.connect('task4/inventory.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT, quantity INTEGER, price REAL, category TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 type TEXT, product_id INTEGER, quantity INTEGER, timestamp TIMESTAMP,
                 FOREIGN KEY (product_id) REFERENCES products(id))''')
    c.execute('INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)', ('admin', 'password123'))
    conn.commit()
    conn.close()


def check_tables():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    # Get a list of all tables in the database
    c.execute("SELECT * FROM products;")
    tables = c.fetchall()
    # Print the list of tables
    for table in tables:
        print(table)
    conn.close()


create_database()
check_tables()