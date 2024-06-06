import sqlite3
from tkinter import messagebox


def check_low_stock():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('''SELECT p.id, p.name, (p.quantity + COALESCE(SUM(
                         CASE WHEN t.type = 'purchase' THEN t.quantity
                         ELSE -t.quantity END), 0)) AS current_stock
                         FROM products p
                         LEFT JOIN transactions t ON p.id = t.product_id
                         GROUP BY p.id, p.name
                         HAVING current_stock < 10''')
    low_stock_products = c.fetchall()
    conn.close()

    # Generate alerts
    alert_message = ""
    for product in low_stock_products:
        alert_message += f"Alert: Low stock for {product[1]} (ID: {product[0]})\n"

    if alert_message:
        messagebox.showinfo("Low Stock Alert", alert_message)
    else:
        messagebox.showinfo("Low Stock Alert", "No low stock items")
