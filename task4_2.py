import sqlite3
from tkinter import messagebox
import tkinter as tk


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
                           command=lambda: update_product(id_entry, name_entry, quantity_entry, price_entry, category_entry,
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