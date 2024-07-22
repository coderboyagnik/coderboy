import tkinter as tk
import time

def update_clock():
    now = time.strftime("%H:%M:%S")
    clock_label.config(text=now)
    root.after(1000, update_clock)

root = tk.Tk()
root.title("Digital Clock")

clock_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
clock_label.pack()

update_clock()
root.mainloop()
