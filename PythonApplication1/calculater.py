import tkinter as tk
from tkinter import messagebox

def open_calculator():
   
    calculator_window = tk.Toplevel()
    calculator_window.title("Calculator")
    calculator_window.geometry("400x370")

    entry = tk.Entry(calculator_window, width=16, font=('Arial', 24), borderwidth=2)
    entry.grid(row=0, column=0, columnspan=4)

    def button_click(number):
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current + str(number))

    def button_clear():
        entry.delete(0, tk.END)

    def button_equal():
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")

    # Calculator buttons
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ('C', 5, 0)
    ]

    for (text, row, column) in buttons:
        if text == '=':
            button = tk.Button(calculator_window, text=text, padx=40, pady=20, command=button_equal)
        elif text == 'C':
            button = tk.Button(calculator_window, text=text, padx=40, pady=20, command=button_clear)
        else:
            button = tk.Button(calculator_window, text=text, padx=40, pady=20, command=lambda t=text: button_click(t))
        button.grid(row=row, column=column)
