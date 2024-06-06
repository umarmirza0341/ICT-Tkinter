import sqlite3
from tkinter import messagebox
import tkinter as tk


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
