# currency_converter.py

import tkinter as tk
from tkinter import messagebox
import requests

def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_entry.get().upper()
    to_currency = to_currency_entry.get().upper()
    
    api_key = "YOUR_API_KEY"  # Replace with your API key
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    
    response = requests.get(url)
    data = response.json()
    
    if to_currency in data['rates']:
        conversion_rate = data['rates'][to_currency]
        converted_amount = amount * conversion_rate
        result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        messagebox.showerror("Error", "Invalid currency code")

root = tk.Tk()
root.title("Currency Converter")

amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.grid(row=1, column=0)
from_currency_entry = tk.Entry(root)
from_currency_entry.grid(row=1, column=1)

to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.grid(row=2, column=0)
to_currency_entry = tk.Entry(root)
to_currency_entry.grid(row=2, column=1)

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
