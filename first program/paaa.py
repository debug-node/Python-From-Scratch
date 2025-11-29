import tkinter as tk
from tkinter import messagebox
import random

# Character sets
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

# Function to generate password
def generate_password():
    try:
        nr_letters = int(entry_letters.get())
        nr_numbers = int(entry_numbers.get())
        nr_symbols = int(entry_symbols.get())

        password_list = []

        for _ in range(nr_letters):
            password_list.append(random.choice(letters))
        for _ in range(nr_numbers):
            password_list.append(random.choice(numbers))
        for _ in range(nr_symbols):
            password_list.append(random.choice(symbols))

        random.shuffle(password_list)
        password = ''.join(password_list)

        entry_result.delete(0, tk.END)
        entry_result.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for all fields.")

# Create GUI window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x300")
window.config(padx=20, pady=20)

# Labels and Entry Fields
tk.Label(window, text="How many letters?").pack()
entry_letters = tk.Entry(window)
entry_letters.pack()

tk.Label(window, text="How many numbers?").pack()
entry_numbers = tk.Entry(window)
entry_numbers.pack()

tk.Label(window, text="How many symbols?").pack()
entry_symbols = tk.Entry(window)
entry_symbols.pack()

# Generate Button
tk.Button(window, text="Generate Password", command=generate_password).pack(pady=10)

# Output field
tk.Label(window, text="Generated Password:").pack()
entry_result = tk.Entry(window, width=40)
entry_result.pack()

# Start the GUI event loop
window.mainloop()
