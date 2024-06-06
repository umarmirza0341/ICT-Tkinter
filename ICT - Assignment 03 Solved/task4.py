import tkinter as tk
import sqlite3
import shutil
import os
from tkinter import filedialog
from tkinter import messagebox


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


def authenticate(username, password):
    conn = sqlite3.connect('inventory.db')
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


def add_product(name_entry, quantity_entry, price_entry, category_entry, add_product_management_window):
    name = name_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()
    category = category_entry.get()

    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('INSERT INTO products (name, quantity, price, category) VALUES (?, ?, ?, ?)',
              (name, quantity, price, category))
    conn.commit()
    conn.close()

    messagebox.showinfo("Product Management", "Product added successfully")
    add_product_management_window.destroy()


def update_product(id_entry, name_entry, quantity_entry, price_entry, category_entry, update_product_management_window):
    id = id_entry.get()
    name = name_entry.get()
    quantity = quantity_entry.get()
    price = price_entry.get()
    category = category_entry.get()

    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('UPDATE products SET name=?, quantity=?, price=?, category=? WHERE id=?',
              (name, quantity, price, category, id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Product Management", "Product updated successfully")
    update_product_management_window.destroy()


def delete_product(id_entry, delete_product_management_window):
    id = id_entry.get()

    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('DELETE FROM products WHERE id=?', (id,))
    conn.commit()
    conn.close()

    messagebox.showinfo("Product Management", "Product deleted successfully")
    delete_product_management_window.destroy()


def add_product_window(product_management_window):
    add_product_management_window = tk.Toplevel(product_management_window)
    add_product_management_window.title("Product Management")

    tk.Label(add_product_management_window, text="Product Name:").grid(row=1, column=0, padx=10, pady=5)
    name_entry = tk.Entry(add_product_management_window)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(add_product_management_window, text="Product Quantity:").grid(row=2, column=0, padx=10, pady=5)
    quantity_entry = tk.Entry(add_product_management_window)
    quantity_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(add_product_management_window, text="Product Price:").grid(row=3, column=0, padx=10, pady=5)
    price_entry = tk.Entry(add_product_management_window)
    price_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(add_product_management_window, text="Product Category:").grid(row=4, column=0, padx=10, pady=5)
    category_entry = tk.Entry(add_product_management_window)
    category_entry.grid(row=4, column=1, padx=10, pady=5)

    add_button = tk.Button(add_product_management_window, text="Add Product",
                           command=lambda: add_product(name_entry, quantity_entry, price_entry, category_entry,
                                                       add_product_management_window))
    add_button.grid(row=5, column=0, padx=10, pady=10)


def update_product_window(product_management_window):
    update_product_management_window = tk.Toplevel(product_management_window)
    update_product_management_window.title("Product Management")

    tk.Label(update_product_management_window, text="Product ID:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(update_product_management_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(update_product_management_window, text="Product Name:").grid(row=1, column=0, padx=10, pady=5)
    name_entry = tk.Entry(update_product_management_window)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(update_product_management_window, text="Product Quantity:").grid(row=2, column=0, padx=10, pady=5)
    quantity_entry = tk.Entry(update_product_management_window)
    quantity_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(update_product_management_window, text="Product Price:").grid(row=3, column=0, padx=10, pady=5)
    price_entry = tk.Entry(update_product_management_window)
    price_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(update_product_management_window, text="Product Category:").grid(row=4, column=0, padx=10, pady=5)
    category_entry = tk.Entry(update_product_management_window)
    category_entry.grid(row=4, column=1, padx=10, pady=5)

    add_button = tk.Button(update_product_management_window, text="Update Product",
                           command=lambda: update_product(id_entry, name_entry, quantity_entry, price_entry,
                                                          category_entry,
                                                          update_product_management_window))
    add_button.grid(row=5, column=0, padx=10, pady=10)


def delete_product_window(product_management_window):
    delete_product_management_window = tk.Toplevel(product_management_window)
    delete_product_management_window.title("Product Management")

    tk.Label(delete_product_management_window, text="Product ID:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(delete_product_management_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    add_button = tk.Button(delete_product_management_window, text="Delete Product",
                           command=lambda: delete_product(id_entry, delete_product_management_window))
    add_button.grid(row=5, column=0, padx=10, pady=10)


def record_purchase(id_entry, quantity_entry, product_record_management_window):
    product_id = id_entry.get()
    quantity = quantity_entry.get()

    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('INSERT INTO transactions (type, product_id, quantity) VALUES (?, ?, ?)',
              ('purchase', product_id, quantity))
    c.execute('UPDATE products SET quantity = quantity + ? WHERE id = ?', (quantity, product_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Product Management", "Purchase recorded successfully")
    product_record_management_window.destroy()


def record_sale(id_entry, quantity_entry, product_record_management_window):
    product_id = id_entry.get()
    quantity = quantity_entry.get()

    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('INSERT INTO transactions (type, product_id, quantity) VALUES (?, ?, ?)',
              ('sale', product_id, quantity))
    c.execute('UPDATE products SET quantity = quantity - ? WHERE id = ?', (quantity, product_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Product Management", "Sale recorded successfully")
    product_record_management_window.destroy()


def record_return(id_entry, quantity_entry, product_record_management_window):
    product_id = id_entry.get()
    quantity = quantity_entry.get()

    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute('INSERT INTO transactions (type, product_id, quantity) VALUES (?, ?, ?)',
              ('return', product_id, quantity))
    c.execute('UPDATE products SET quantity = quantity + ? WHERE id = ?', (quantity, product_id))
    conn.commit()
    conn.close()

    messagebox.showinfo("Product Management", "Return recorded successfully")
    product_record_management_window.destroy()


def record_sale_window(product_management_window):
    product_record_management_window = tk.Toplevel(product_management_window)
    product_record_management_window.title("Product Management")

    tk.Label(product_record_management_window, text="Product ID:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(product_record_management_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(product_record_management_window, text="Product Quantity:").grid(row=2, column=0, padx=10, pady=5)
    quantity_entry = tk.Entry(product_record_management_window)
    quantity_entry.grid(row=2, column=1, padx=10, pady=5)

    sale_button = tk.Button(product_record_management_window, text="Record Sale",
                            command=lambda: record_sale(id_entry, quantity_entry, product_record_management_window))
    sale_button.grid(row=6, column=1, padx=10, pady=10)


def record_purchase_window(product_management_window):
    product_record_management_window = tk.Toplevel(product_management_window)
    product_record_management_window.title("Product Management")

    tk.Label(product_record_management_window, text="Product ID:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(product_record_management_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(product_record_management_window, text="Product Quantity:").grid(row=2, column=0, padx=10, pady=5)
    quantity_entry = tk.Entry(product_record_management_window)
    quantity_entry.grid(row=2, column=1, padx=10, pady=5)

    sale_button = tk.Button(product_record_management_window, text="Record Purchase",
                            command=lambda: record_purchase(id_entry, quantity_entry, product_record_management_window))
    sale_button.grid(row=6, column=1, padx=10, pady=10)


def record_return_window(product_management_window):
    product_record_management_window = tk.Toplevel(product_management_window)
    product_record_management_window.title("Product Management")

    tk.Label(product_record_management_window, text="Product ID:").grid(row=0, column=0, padx=10, pady=5)
    id_entry = tk.Entry(product_record_management_window)
    id_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(product_record_management_window, text="Product Quantity:").grid(row=2, column=0, padx=10, pady=5)
    quantity_entry = tk.Entry(product_record_management_window)
    quantity_entry.grid(row=2, column=1, padx=10, pady=5)

    sale_button = tk.Button(product_record_management_window, text="Record Return",
                            command=lambda: record_return(id_entry, quantity_entry, product_record_management_window))
    sale_button.grid(row=6, column=1, padx=10, pady=10)


def search_products(name_entry, search_product_management_window):
    product_name = name_entry.get().strip()

    # Check if the product name is provided
    if not product_name:
        messagebox.showerror("Search", "Please enter a product name to search")
        return

    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    # Search for products by name
    c.execute('SELECT * FROM products WHERE name LIKE ?', ('%' + product_name + '%',))
    products = c.fetchall()
    conn.close()

    # Display search results in a messagebox
    if products:
        result_message = "Search Results:\n\n"
        for product in products:
            result_message += f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}, Price: {product[3]}, Category: {product[4]}\n"
        messagebox.showinfo("Search Results", result_message)
    else:
        messagebox.showinfo("Search Results", "No products found matching the specified name")

    search_product_management_window.destroy()


def search_product_window(product_management_window):
    search_product_management_window = tk.Toplevel(product_management_window)
    search_product_management_window.title("Product Management")

    tk.Label(search_product_management_window, text="Product Name:").grid(row=1, column=0, padx=10, pady=5)
    name_entry = tk.Entry(search_product_management_window)
    name_entry.grid(row=1, column=1, padx=10, pady=5)

    search_button = tk.Button(search_product_management_window, text="Search",
                              command=lambda: search_products(name_entry, search_product_management_window))
    search_button.grid(row=7, column=1, padx=10, pady=10)


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


def backup_database():
    backup_dir = filedialog.askdirectory(title="Select Backup Directory")
    if backup_dir:
        try:
            backup_file = os.path.join(backup_dir, 'inventory_backup.db')
            shutil.copy('inventory.db', backup_file)
            messagebox.showinfo("Backup", "Database backup created successfully")
        except Exception as e:
            messagebox.showerror("Backup", f"Failed to create backup: {e}")


def restore_database():
    backup_file = filedialog.askopenfilename(title="Select Backup File", filetypes=[("SQLite Database", "*.db")])
    if backup_file:
        try:
            shutil.copy(backup_file, 'inventory.db')
            messagebox.showinfo("Restore", "Database restored successfully")
        except Exception as e:
            messagebox.showerror("Restore", f"Failed to restore database: {e}")


def open_product_management():
    # Create a new window for product management
    product_management_window = tk.Toplevel(root)
    product_management_window.title("Product Management")

    # Create and place buttons for adding, updating, and deleting products
    add_button = tk.Button(product_management_window, text="Add Product",
                           command=lambda: add_product_window(product_management_window))
    add_button.grid(row=5, column=0, padx=10, pady=10)

    update_button = tk.Button(product_management_window, text="Update Product",
                              command=lambda: update_product_window(product_management_window))
    update_button.grid(row=5, column=1, padx=10, pady=10)

    delete_button = tk.Button(product_management_window, text="Delete Product",
                              command=lambda: delete_product_window(product_management_window))
    delete_button.grid(row=5, column=2, padx=10, pady=10)

    # Create and place buttons for recording transactions
    purchase_button = tk.Button(product_management_window, text="Record Purchase",
                                command=lambda: record_purchase_window(product_management_window))
    purchase_button.grid(row=6, column=0, padx=10, pady=10)

    sale_button = tk.Button(product_management_window, text="Record Sale",
                            command=lambda: record_sale_window(product_management_window))
    sale_button.grid(row=6, column=1, padx=10, pady=10)

    return_button = tk.Button(product_management_window, text="Record Return",
                              command=lambda: record_return_window(product_management_window))
    return_button.grid(row=6, column=2, padx=10, pady=10)

    # Create and place button for checking low stock items
    low_stock_button = tk.Button(product_management_window, text="Check Low Stock", command=check_low_stock)
    low_stock_button.grid(row=7, column=0, padx=10, pady=10)

    # Create and place button for searching products
    search_button = tk.Button(product_management_window, text="Search",
                              command=lambda: search_product_window(product_management_window))
    search_button.grid(row=7, column=1, padx=10, pady=10)

    # Create and place button for generating sales report
    sales_report_button = tk.Button(product_management_window, text="Generate Sales Report",
                                    command=generate_sales_report)
    sales_report_button.grid(row=7, column=2, padx=10, pady=10)

    # Create and place button for backing up the database
    backup_button = tk.Button(product_management_window, text="Backup Database", command=backup_database)
    backup_button.grid(row=8, column=0, padx=10, pady=10)

    # Create and place button for restoring the database
    restore_button = tk.Button(product_management_window, text="Restore Database", command=restore_database)
    restore_button.grid(row=8, column=1, padx=10, pady=10)


root = tk.Tk()
root.title("Inventory System Login")

tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the login button
login_button = tk.Button(root, text="Login", command=lambda: login(username_entry, password_entry,
                                                                   open_product_management))
login_button.grid(row=2, columnspan=2, padx=10, pady=10)

create_database()

root.mainloop()
