import sqlite3
import shutil
import os
from tkinter import filedialog
from tkinter import messagebox


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
