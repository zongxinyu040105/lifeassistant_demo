import requests
import json
import weather
import calculater
import deepseek
import tkinter as tk
from tkinter import messagebox



root = tk.Tk()
root.title("assitent")
root.geometry("300x200")

btn_weather = tk.Button(root, text="Show Weather", command=weather.show_weather)
btn_weather.pack(pady=10)

btn_calculator = tk.Button(root, text="Open Calculator", command=calculater.open_calculator)
btn_calculator.pack(pady=10)

btn_chat = tk.Button(root, text="Open Chat", command=deepseek.deepseek.open_chat_window)  
btn_chat.pack(pady=10)

root.mainloop()
