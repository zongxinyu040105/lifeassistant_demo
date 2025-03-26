from matplotlib.colors import cnames
import requests
import json
import weather
import calculater
import deepseek
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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

def registration():
    name = entry_name.get()
    password = entry_password.get()

    db = connect_to_db()
    cursor = db.cursor()

    try:

        cursor.execute("SELECT * FROM user_data WHERE name = %s", (name,))
        existing_user = cursor.fetchone()

        if existing_user:
           messagebox.showerror("Error", "Username already taken!")
        else:
           cursor.execute("INSERT INTO user_data (name, password) VALUES (%s, %s)", (name, password))
           db.commit()  # Commit the transaction
           messagebox.showinfo("Success", "User registered successfully!")
        
    except pymysql.MySQLError as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    finally:
        cursor.close()
        db.close()

def cname_id(cname):
    #cname = entry_cname.get()
    db = connect_to_db()
    cursor = db.cursor()
    try:

        cursor.execute("SELECT city_id FROM city_id_name WHERE city_name = %s ", (cname))
        result = cursor.fetchone()  

        if result:
            print(f"Result value: {result}")
            #messagebox.showinfo("succes find", "welcome!")
            weather.show_weather(result['city_id'])
        else:
            messagebox.showerror("fail", "can't find")
    #except pymysql.MySQLError as err:
        #messagebox.showerror("databaseerror", f"error: {err}")
    finally:
        cursor.close()
        db.close()


def successlogin():
    new_window = tk.Tk() 
    new_window.title("assitent")
    new_window.geometry("300x200")


    label_cname = tk.Label(new_window, text="cityname:")#
    label_cname.pack()#
    entry_cname = tk.Entry(new_window)#
    entry_cname.pack()#
    cname = entry_cname.get()

    #btn_weather = tk.Button( new_window, text="Show Weather", command=weather.show_weather)
    btn_weather = tk.Button( new_window, text="Show Weather", command=lambda: cname_id(entry_cname.get()))
    btn_weather.pack(pady=10)

    btn_calculator = tk.Button( new_window, text="Open Calculator", command=calculater.Calculator.open_calculator_window)
    btn_calculator.pack(pady=10)

    btn_chat = tk.Button( new_window, text="Deep seek", command=deepseek.deepseek.open_chat_window)  
    btn_chat.pack(pady=10)

    #new_window.mainloop()





root = tk.Tk()
root.title("LogWeb") 
root.geometry("380x200")  
root.style = ttk.Style() 
root.style.theme_use('clam')  

grid = ttk.Frame(root)
grid.pack(padx=10, pady=5)


ttk.Label(grid, text="Name:").grid(row=0, column=0,padx=10, pady=20, sticky=tk.W)
entry_name = ttk.Entry(grid, width=25)
entry_name.grid(row=0, column=1, padx=5, pady=5)


ttk.Label(grid, text="Password:").grid(row=1, column=0, sticky=tk.W)
entry_password = ttk.Entry(grid, 
                           width=25, 
                           show='*',)
entry_password.grid(row=1, column=1, padx=5, pady=5)


#login_icon = tk.PhotoImage(file="login.png")  
#reg_icon = tk.PhotoImage(file="register.png")

ttk.Button(grid,         
          text="Login", 
          command=login,
          compound=tk.LEFT).grid(row=2, column=0,padx=35, pady=30)

ttk.Button(grid, 

          text="Registration", 
          command=registration,
          compound=tk.LEFT).grid(row=2, column=1, pady=30)

root.mainloop()