import sqlite3
from tkinter import messagebox


# Function to create database and user table if they don't exist
def create_database():
    conn = sqlite3.connect('inventory.db')
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
    # Insert a default admin user if not already present
    c.execute('INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)', ('admin', 'password123'))
    conn.commit()
    conn.close()


# Function to authenticate user credentials
def authenticate(username, password):
    conn = sqlite3.connect('task4/inventory.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    result = c.fetchone()
    conn.close()
    return result


# Function to handle login button click
def login(username_entry, password_entry, open_product_management):
    username = username_entry.get()
    password = password_entry.get()

    if authenticate(username, password):
        messagebox.showinfo("Login", "Login Successful")
        open_product_management()
    else:
        messagebox.showerror("Login", "Invalid username or password")
