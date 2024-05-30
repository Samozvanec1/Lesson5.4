import  tkinter as tk
from    tkinter import ttk #импортируем библиотеку ttk для работы с таблицами
from    tkinter import messagebox #импортируем библиотеку messagebox для работы с сообщениями
import sqlite3 #импортируем библиотеку sqlite3 для работы с базой данных

def init_db():
    conn = sqlite3.connect('bizness_orders.db') #соединяемся с базой данных в которой будем хранить данные
    cur = conn.cursor() #создаем курсор для работы с базой данных он же идентификатор
    cur.execute('''
    CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY,
    customer_name TEXT, 
    order_details TEXT, 
    status TEXT NOT NULL)
    ''') #создаем таблицу в базе данных
    conn.commit() #фиксируем изменения
    conn.close() #закрываем соединение с базой данных

def add_order():  #функция добавления данных в таблицу orders в базе данных
    conn = sqlite3.connect('bizness_orders.db') #соединяемся с базой данных
    cur = conn.cursor() #создаем курсор для работы с базой данных
    cur.execute("INSERT INTO orders (customer_name, order_details, status) VALUES ( ?, ?, 'Новый')",
                (customer_name_entry.get(), order_details_entry.get())) #добавляем данные в таблицу orders
    conn.commit() #фиксируем изменения
    conn.close() #закрываем соединение|подключение с базой данных
    customer_name_entry.delete(0, 'end') #очищаем поле ввода имени клиента от начала до конца
    order_details_entry.delete(0, 'end') #очищаем поле ввода деталей заказа от начала до конца
    view_orders() #запускаем функцию view_orders для отображения данных  функция запускается после каждого добавления данных
def view_orders(): #функция отображения данных и обновления элементов таблицы
    for i in tree.get_children(): #очищаем таблицу от старых данных
        tree.delete(i)  #все сохраняем в переменную i, затем удаляем i (очищаем)
    conn = sqlite3.connect('bizness_orders.db') #соединяемся с базой данных
    cur = conn.cursor() #создаем курсор для работы с базой данных
    cur.execute("SELECT * FROM orders") #получаем данные из таблицы orders получаем все строки
    rows = cur.fetchall() #получаем все строки
    for row in rows: #пробегаем по полученным строкам (rows это все строки нашей таблицы)
        tree.insert('', tk.END, values=row) #зяли таблицу из переменной tree (insert - добавляет данные в таблицу)
    conn.close() #закрываем соединение|подключение с базой данных


def complete_order():
    selected_item = tree.selection() #выбранный элемент в таблице получаем в переменную selected_item
    if selected_item:  #если выбранный элемент есть то выполняем код
        order_id = tree.item(selected_item[0])['values'][0]   #получаем id заказа (первый столбец таблицы) id - первый столбец он равен [0]
        conn = sqlite3.connect('bizness_orders.db') #соединяемся с базой данных, заппрос на иззменение базы данных
        cur = conn.cursor() #создаем курсор для работы с базой данных
        cur.execute("UPDATE orders SET status = 'Завершен' WHERE id = ?", (order_id,)) #изменяем данные в таблице orders\ пишем запрос\ изменяем статус на завершенный \конкретный заказ определяет по id
        conn.commit() #фиксируем изменения
        conn.close() #закрываем соединение|подключение с базой данных
        view_orders() #запускаем функцию view_orders для обновления данных в таблице
    else:
        messagebox.showwarning('Предупреждение', 'Выберите заказ для завершения')   #выводим предупреждение что нужно выбрать заказ для завершения

app = tk.Tk()
app.title('Система управления заказами')

tk.Label(app, text='Имя клиента').pack() #вводим надпись

customer_name_entry = tk.Entry(app) #переменная для ввода (добавления) имени клиента
customer_name_entry.pack() #размещение на экране

tk.Label(app, text='Детали заказа').pack() #вводим надпись

order_details_entry = tk.Entry(app) #переменная для ввода (добавления) деталей заказа
order_details_entry.pack() #размещение на экране

add_button = tk.Button(app, text='Добавить заказ', command=add_order)
add_button.pack() #размещение на экране

complete_button = tk.Button(app, text='Завершить заказ', command=complete_order)
complete_button.pack() #размещение на экране

columns = ('id', 'customer_name', 'order_details', 'status')
tree = ttk.Treeview(app, columns=columns, show='headings') #создание таблицы в которой нам нужны только колонки + показывать заголовки
for column in columns: #пребирает кортеж (колонки/columns) и каждое название сохраняется в переменную column
    tree.heading(column=column, text=column.title()) #потом установливает название колонки в заголовок то что в переменной column
tree.pack() #размещение на экране


init_db()
view_orders() #запускаем функцию view_orders для отображения данных
app.mainloop()