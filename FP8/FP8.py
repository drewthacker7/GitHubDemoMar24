import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# -------------------- 1. Create the DB if needed --------------------
def init_db():
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            dob TEXT,
            email TEXT,
            phone TEXT,
            address TEXT,
            city TEXT,
            state TEXT,
            zip TEXT,
            contact_method TEXT
        )
    ''')
    conn.commit()
    conn.close()

# -------------------- 2. Handle form submission --------------------
def submit_form():
    data = (
        entry_first.get(),
        entry_last.get(),
        entry_dob.get(),
        entry_email.get(),
        entry_phone.get(),
        entry_address.get(),
        entry_city.get(),
        entry_state.get(),
        entry_zip.get(),
        contact_method_var.get()
    )

    # Simple validation example
    if not entry_first.get() or not entry_email.get():
        messagebox.showerror("Error", "First Name and Email are required.")
        return

    try:
        conn = sqlite3.connect("customers.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO customers 
            (first_name, last_name, dob, email, phone, address, city, state, zip, contact_method)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', data)
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Customer information saved!")
        clear_form()
    except Exception as e:
        messagebox.showerror("Database Error", f"Something went wrong:\n{e}")

# -------------------- 3. Clear form inputs --------------------
def clear_form():
    entry_first.delete(0, tk.END)
    entry_last.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_city.delete(0, tk.END)
    entry_state.delete(0, tk.END)
    entry_zip.delete(0, tk.END)
    contact_method_var.set("Email")

# -------------------- 4. Set up GUI --------------------
root = tk.Tk()
root.title("Customer Information System")
root.geometry("400x550")

# Labels and Entry Fields
tk.Label(root, text="First Name:").grid(row=0, column=0, sticky="e", padx=10, pady=5)
entry_first = tk.Entry(root)
entry_first.grid(row=0, column=1)

tk.Label(root, text="Last Name:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_last = tk.Entry(root)
entry_last.grid(row=1, column=1)

tk.Label(root, text="Date of Birth (YYYY-MM-DD):").grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_dob = tk.Entry(root)
entry_dob.grid(row=2, column=1)

tk.Label(root, text="Email Address:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1)

tk.Label(root, text="Phone Number:").grid(row=4, column=0, sticky="e", padx=10, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=4, column=1)

tk.Label(root, text="Street Address:").grid(row=5, column=0, sticky="e", padx=10, pady=5)
entry_address = tk.Entry(root)
entry_address.grid(row=5, column=1)

tk.Label(root, text="City:").grid(row=6, column=0, sticky="e", padx=10, pady=5)
entry_city = tk.Entry(root)
entry_city.grid(row=6, column=1)

tk.Label(root, text="State/Province:").grid(row=7, column=0, sticky="e", padx=10, pady=5)
entry_state = tk.Entry(root)
entry_state.grid(row=7, column=1)

tk.Label(root, text="Zip/Postal Code:").grid(row=8, column=0, sticky="e", padx=10, pady=5)
entry_zip = tk.Entry(root)
entry_zip.grid(row=8, column=1)

tk.Label(root, text="Preferred Contact Method:").grid(row=9, column=0, sticky="e", padx=10, pady=5)
contact_method_var = tk.StringVar()
contact_method_dropdown = ttk.Combobox(root, textvariable=contact_method_var)
contact_method_dropdown['values'] = ("Email", "Phone", "Mail")
contact_method_dropdown.current(0)
contact_method_dropdown.grid(row=9, column=1)

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=submit_form, bg="green", fg="white")
submit_btn.grid(row=10, columnspan=2, pady=20)

# -------------------- 5. Run everything --------------------
init_db()         # Create DB & table if not exists
root.mainloop()   # Start GUI
