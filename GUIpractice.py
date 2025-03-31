import tkinter as tk

def submit_feedback():
    name = name_entry.get()
    email = email_entry.get()
    feedback = feedback_text.get("1.0", tk.END).strip()

    print("---- Feedback Submitted ----")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Feedback: {feedback}")
    print("----------------------------\n")

    # Clear the fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    feedback_text.delete("1.0", tk.END)

# Create main window
root = tk.Tk()
root.title("Feedback Form")
root.geometry("400x300")

# Title label
title_label = tk.Label(root, text="Please provide feedback on your experience", font=("Arial", 12, "bold"))
title_label.pack(pady=10)

# Name
name_label = tk.Label(root, text="Name:")
name_label.pack(anchor="w", padx=20)
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=20)

# Email
email_label = tk.Label(root, text="Email:")
email_label.pack(anchor="w", padx=20, pady=(10, 0))
email_entry = tk.Entry(root, width=40)
email_entry.pack(padx=20)

# Feedback
feedback_label = tk.Label(root, text="Feedback:")
feedback_label.pack(anchor="w", padx=20, pady=(10, 0))
feedback_text = tk.Text(root, height=5, width=40)
feedback_text.pack(padx=20)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_feedback)
submit_button.pack(pady=10)

# Start the app
root.mainloop()
