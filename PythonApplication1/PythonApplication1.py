import requests
import json
import weather
import calculater
import deepseek
import tkinter as tk
from tkinter import messagebox
import pymysql

def connect_to_db():
    return pymysql.connect(
        host="bj-cdb-on3wtpbc.sql.tencentcdb.com",
        port=28103,
        user="root",
        password="zong321610235", 
        database="la_user",
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

def login():
    name = entry_name.get()
    password = entry_password.get()


    db = connect_to_db()
    cursor = db.cursor()

    try:

        cursor.execute("SELECT * FROM user_data WHERE name = %s AND password = %s", (name, password))
        result = cursor.fetchone()  

        if result:
            messagebox.showinfo("succes", "welcome!")
            successlogin()
            root.withdraw()
        else:
            messagebox.showerror("fail", "tnumbertnamewrong!")
    except pymysql.MySQLError as err:
        messagebox.showerror("databaseerror", f"error: {err}")
    finally:
        cursor.close()
        db.close()
def successlogin():
    new_window = tk.Tk() 
    new_window.title("assitent")
    new_window.geometry("300x200")

    btn_weather = tk.Button( new_window, text="Show Weather", command=weather.show_weather)
    btn_weather.pack(pady=10)

    btn_calculator = tk.Button( new_window, text="Open Calculator", command=calculater.open_calculator)
    btn_calculator.pack(pady=10)

    btn_chat = tk.Button( new_window, text="Open Chat", command=deepseek.deepseek.open_chat_window)  
    btn_chat.pack(pady=10)

    #new_window.mainloop()


root = tk.Tk()
root.title("logweb")


label_name = tk.Label(root, text="name:")
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()


label_password = tk.Label(root, text="password:")
label_password.pack()
entry_password = tk.Entry(root)
entry_password.pack()


login_button = tk.Button(root, text="log", command=login)
login_button.pack()


root.mainloop()
















