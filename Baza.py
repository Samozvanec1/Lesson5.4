import sqlite3
import tkinter as tk
from tkinter import ttk

def writeAllChanges():
    print("Кнопка работает")
    print(f"Имя клиента:{name_entry.get()},услуга выданная клиенту:{order_details_entry.get()}")
conn = sqlite3.connect('orders_table.db') # Connecting to  table 
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS orders_table(
        id INT PRIMARY KEY,
        customer_name TEXT NOT NULL,
        order_details TEXT NOT NULL,
        status TEXT
    );
''')

window = tk.Tk() # Creating window
window.title = "just testing"


name_label = tk.Label(window,text="Введите имя клиента")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

order_details_label = tk.Label(window,text="Введите описание услуги")
order_details_label.pack()

order_details_entry = tk.Entry(window)
order_details_entry.pack()

confirm_button = tk.Button(window,text = "Нажмите чтобы записать", command=writeAllChanges)
confirm_button.pack()

tk.mainloop()


