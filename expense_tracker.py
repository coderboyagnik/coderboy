# expense_tracker.py

import tkinter as tk
from tkinter import messagebox
import json

def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()
    
    if not date or not category or not amount:
        messagebox.showerror("Error", "Please fill in all fields")
        return
    
    new_expense = {
        "date": date,
        "category": category,
        "amount": amount
    }
    
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        expenses = []
    
    expenses.append(new_expense)
    
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)
    
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    
    messagebox.showinfo("Success", "Expense added successfully")

def show_summary():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No expenses file found")
        return
    
    total_expense = sum(float(expense["amount"]) for expense in expenses)
    categories = {}
    
    for expense in expenses:
        category = expense["category"]
        amount = float(expense["amount"])
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount
    
    summary = f"Total Expense: ${total_expense:.2f}\n\n"
    for category, amount in categories.items():
        summary += f"{category}: ${amount:.2f}\n"
    
    messagebox.showinfo("Summary", summary)

# GUI setup
root = tk.Tk()
root.title("Expense Tracker")

date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
date_label.grid(row=0, column=0)
date_entry = tk.Entry(root, width=35)
date_entry.grid(row=0, column=1, columnspan=2)

category_label = tk.Label(root, text="Category:")
category_label.grid(row=1, column=0)
category_entry = tk.Entry(root, width=35)
category_entry.grid(row=1, column=1, columnspan=2)

amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=2, column=0)
amount_entry = tk.Entry(root, width=35)
amount_entry.grid(row=2, column=1, columnspan=2)

add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.grid(row=3, column=1)

summary_button = tk.Button(root, text="Show Summary", command=show_summary)
summary_button.grid(row=3, column=2)

root.mainloop()
