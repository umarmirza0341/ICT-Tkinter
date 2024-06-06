import sqlite3
from tkinter import messagebox
import tkinter as tk


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