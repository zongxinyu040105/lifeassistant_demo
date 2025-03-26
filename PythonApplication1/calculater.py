import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x370")

        # Entry widget for the calculator display
        self.entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Calculator buttons layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, column) in buttons:
            if text == '=':
                button = tk.Button(root, text=text, padx=40, pady=20, command=self.button_equal)
            elif text == 'C':
                button = tk.Button(root, text=text, padx=40, pady=20, command=self.button_clear)
            else:
                button = tk.Button(root, text=text, padx=40, pady=20, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=column)

    def button_click(self, number):
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current + str(number))

    def button_clear(self):
        self.entry.delete(0, tk.END)

    def button_equal(self):
        try:
            result = eval(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")

    @staticmethod
    def open_calculator_window():
        calculator_window = tk.Toplevel()
        app = Calculator(calculator_window)
        calculator_window.mainloop()