import tkinter as tk

def check_palindrome():
    word = entry.get()
    if word == word[::-1]:
        result.set("Palindrome")
    else:
        result.set("Not a palindrome")

root = tk.Tk()
root.title("Palindrome Checker")

entry = tk.Entry(root)
entry.pack()

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

tk.Button(root, text="Check", command=check_palindrome).pack()

root.mainloop()

