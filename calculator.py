import tkinter as tk
from tkinter import messagebox

def evaluate():
    try:
        expr = entry.get()
        weball = eval(expr)
        result_label.config(text="Result: " + str(weball))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x150")

entry = tk.Entry(root, width=25, font=('Arial', 14))
entry.pack(pady=10)

calc_btn = tk.Button(root, text="Calculate", command=evaluate, font=('Arial', 12))
calc_btn.pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=('Arial', 12))
result_label.pack(pady=10)

root.mainloop()