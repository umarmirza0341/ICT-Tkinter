import sqlite3
from tkinter import messagebox


def generate_sales_report():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    # Generate sales summary
    c.execute('''SELECT p.name, SUM(t.quantity) as total_sold, SUM(t.quantity * p.price) as total_revenue
                 FROM transactions t
                 JOIN products p ON t.product_id = p.id
                 WHERE t.type = 'sale'
                 GROUP BY p.name
                 ORDER BY total_sold DESC''')
    sales_summary = c.fetchall()

    # Generate top-selling products
    top_selling_products = sales_summary[:5]  # Top 5 selling products

    # Generate revenue analysis
    c.execute('''SELECT SUM(t.quantity * p.price) as total_revenue
                 FROM transactions t
                 JOIN products p ON t.product_id = p.id
                 WHERE t.type = 'sale' ''')
    total_revenue = c.fetchone()[0]

    conn.close()

    # Display sales report in a messagebox
    report_message = "Sales Report:\n\nSales Summary:\n"
    for product in sales_summary:
        report_message += f"Product: {product[0]}, Total Sold: {product[1]}, Total Revenue: ${product[2]:.2f}\n"

    report_message += "\nTop-Selling Products:\n"
    for product in top_selling_products:
        report_message += f"Product: {product[0]}, Total Sold: {product[1]}, Total Revenue: ${product[2]:.2f}\n"

    report_message += f"\nTotal Revenue: ${total_revenue:.2f}"

    messagebox.showinfo("Sales Report", report_message)
