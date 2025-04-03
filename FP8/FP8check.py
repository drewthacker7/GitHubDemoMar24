import sqlite3

def show_customers():
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()

    if rows:
        print("📦 Customer Records:")
        for row in rows:
            print(row)
    else:
        print("📭 No customers found.")

    conn.close()

show_customers()

