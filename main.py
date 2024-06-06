import tkinter as tk
from task4_1 import create_database, login
from task4_2 import add_product_window, update_product_window, \
    delete_product_window
from task4_3 import record_purchase_window, record_sale_window, \
    record_return_window
from task4_4 import search_product_window
from task4_5 import generate_sales_report
from task4_6 import check_low_stock
from task4_7 import backup_database, restore_database


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

# Call function to create database
create_database()

# Run the main event loop
root.mainloop()
