# password_manager.py

import tkinter as tk
from tkinter import messagebox
import json
from cryptography.fernet import Fernet

# Generate a key and instantiate a Fernet instance
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to save a password
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    
    if not website or not username or not password:
        messagebox.showerror("Error", "Please fill in all fields")
        return
    
    encrypted_password = cipher_suite.encrypt(password.encode()).decode()
    
    new_data = {
        website: {
            "username": username,
            "password": encrypted_password
        }
    }
    
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        data = {}
    
    data.update(new_data)
    
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)
    
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    
    messagebox.showinfo("Success", "Password saved successfully")

# Function to find a password
def find_password():
    website = website_entry.get()
    
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found")
        return
    
    if website in data:
        username = data[website]["username"]
        encrypted_password = data[website]["password"]
        password = cipher_suite.decrypt(encrypted_password.encode()).decode()
        messagebox.showinfo("Details", f"Username: {username}\nPassword: {password}")
    else:
        messagebox.showerror("Error", "No details for the website found")

# GUI setup
root = tk.Tk()
root.title("Password Manager")

website_label = tk.Label(root, text="Website:")
website_label.grid(row=0, column=0)
website_entry = tk.Entry(root, width=35)
website_entry.grid(row=0, column=1, columnspan=2)

username_label = tk.Label(root, text="Username:")
username_label.grid(row=1, column=0)
username_entry = tk.Entry(root, width=35)
username_entry.grid(row=1, column=1, columnspan=2)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=2, column=0)
password_entry = tk.Entry(root, width=35)
password_entry.grid(row=2, column=1, columnspan=2)

save_button = tk.Button(root, text="Save Password", command=save_password)
save_button.grid(row=3, column=1)

find_button = tk.Button(root, text="Find Password", command=find_password)
find_button.grid(row=3, column=2)

root.mainloop()
