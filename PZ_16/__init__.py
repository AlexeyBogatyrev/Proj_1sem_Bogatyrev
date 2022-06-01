import tkinter as tk
from tkinter import ttk
import sqlite3 as sq


class Main(tk.Frame):
    """Класс для главного окна"""

    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#a0dea0', bd=4)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file="11.gif")
        self.btn_open_dialog = tk.Button(toolbar, text='Добавить книгу', command=self.open_dialog, bg='#5da130', bd=0,
                                         compound=tk.TOP, image=self.add_img)
        self.btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file="12.gif")
        btn_edit_dialog = tk.Button(toolbar, text="Редактировать", command=self.open_update_dialog, bg='#5da130',
                                    bd=0, compound=tk.TOP, image=self.update_img)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.delete_img = tk.PhotoImage(file="13.gif")
        btn_delete = tk.Button(toolbar, text="Удалить запись", command=self.delete_records, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.delete_img)
        btn_delete.pack(side=tk.LEFT)

        self.search_img = tk.PhotoImage(file="14.gif")
        btn_search = tk.Button(toolbar, text="Поиск книги", command=self.open_search_dialog, bg='#5da130',
                               bd=0, compound=tk.TOP, image=self.search_img)
        btn_search.pack(side=tk.LEFT)

        self.refresh_img = tk.PhotoImage(file="15.gif")
        btn_refresh = tk.Button(toolbar, text="Обновить экран", command=self.view_records, bg='#5da130',
                                bd=0, compound=tk.TOP, image=self.refresh_img)
        btn_refresh.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('kod', 'janr', 'strana', 'seria', 'autor', 'nazvanie', 'god', 'anat'),
                                 height=15, show='headings')

        self.tree.column('kod', width=50, anchor=tk.CENTER)
        self.tree.column('janr', width=180, anchor=tk.CENTER)
        self.tree.column('strana', width=140, anchor=tk.CENTER)
        self.tree.column('seria', width=140, anchor=tk.CENTER)
        self.tree.column('autor', width=140, anchor=tk.CENTER)
        self.tree.column('nazvanie', width=140, anchor=tk.CENTER)
        self.tree.column('god', width=140, anchor=tk.CENTER)
        self.tree.column('anat', width=140, anchor=tk.CENTER)

        self.tree.heading('kod', text='Код книги')
        self.tree.heading('janr', text='Жанр книги')
        self.tree.heading('strana', text='Страна')
        self.tree.heading('seria', text='Серия книги')
        self.tree.heading('autor', text='Автор')
        self.tree.heading('nazvanie', text='Название')
        self.tree.heading('god', text='Год')
        self.tree.heading('anat', text='Аннотация')

        self.tree.pack()

    def records(self, kod, janr, strana, seria, autor, nazvanie, god, anat):
        self.db.insert_data(kod, janr, strana, seria, autor, nazvanie, god, anat)
        self.view_records()

    def update_record(self, kod, janr, strana, seria, autor, nazvanie, god, anat):
        self.db.cur.execute(
            """UPDATE users SET kod=?, janr=?, strana=?, seria=?, autor=?, nazvanie=?, god=?, anat=? WHERE kod=?""",
            (kod, janr, strana, seria, autor, nazvanie, god, anat, self.tree.set(self.tree.selection()[0], '#1')))
        self.db.con.commit()
        self.view_records()

    def view_records(self):
        self.db.cur.execute("""SELECT * FROM users""")
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def delete_records(self):
        for selection_item in self.tree.selection():
            self.db.cur.execute("""DELETE FROM users WHERE kod=?""", (self.tree.set(selection_item, '#1'),))
        self.db.con.commit()
        self.view_records()

    def search_records(self, janr):
         janr = ("%" + janr + "%",)
         self.db.cur.execute("""SELECT * FROM users WHERE janr LIKE ?""", janr)
         [self.tree.delete(i) for i in self.tree.get_children()]
         [self.tree.insert('', 'end', values=row) for row in self.db.cur.fetchall()]

    def open_dialog(self):
        Child(root, app)

    def open_update_dialog(self):
        Update()

    def open_search_dialog(self):
        Search()


class Child(tk.Toplevel):
    """Класс для дочернего окна"""

    def __init__(self, root, app):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить игрока')
        self.geometry('500x350+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Код')
        label_description.place(x=50, y=25)
        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=110, y=25)

        label_name = tk.Label(self, text='Жанр')
        label_name.place(x=50, y=50)
        self.entry_name = ttk.Entry(self)
        self.entry_name.place(x=110, y=50)

        label_name = tk.Label(self, text='Страна')
        label_name.place(x=50, y=75)
        self.entry_janr = ttk.Entry(self)
        self.entry_janr.place(x=110, y=75)

        label_old = tk.Label(self, text='Серия')
        label_old.place(x=50, y=100)
        self.entry_old = ttk.Entry(self)
        self.entry_old.place(x=110, y=100)

        label_score = tk.Label(self, text='Автор')
        label_score.place(x=50, y=125)
        self.entry_score = ttk.Entry(self)
        self.entry_score.place(x=110, y=125)

        label_score = tk.Label(self, text='Название')
        label_score.place(x=50, y=150)
        self.entry_nazvanie = ttk.Entry(self)
        self.entry_nazvanie.place(x=110, y=150)

        label_score = tk.Label(self, text='Год')
        label_score.place(x=50, y=175)
        self.entry_god = ttk.Entry(self)
        self.entry_god.place(x=110, y=175)

        label_score = tk.Label(self, text='Аннатация')
        label_score.place(x=40, y=200)
        self.entry_anat = ttk.Entry(self)
        self.entry_anat.place(x=110, y=200)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=240)

        self.btn_ok = ttk.Button(self, text='Добавить')
        self.btn_ok.place(x=220, y=240)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_janr.get(),
                                                                       self.entry_old.get(),
                                                                       self.entry_score.get(),
                                                                       self.entry_nazvanie.get(),
                                                                       self.entry_god.get(),
                                                                       self.entry_anat.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__(root, app)
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title("Редактировать запись")
        btn_edit = ttk.Button(self, text="Редактировать")
        btn_edit.place(x=205, y=240)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                       self.entry_name.get(),
                                                                       self.entry_janr.get(),
                                                                       self.entry_old.get(),
                                                                       self.entry_score.get(),
                                                                       self.entry_nazvanie.get(),
                                                                       self.entry_god.get(),
                                                                       self.entry_anat.get()))

        self.btn_ok.destroy()


class Search(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_search()
        self.view = app

    def init_search(self):
        self.title("Поиск")
        self.geometry("300x100+400+300")
        self.resizable(False, False)

        label_search = tk.Label(self, text="Поиск")
        label_search.place(x=50, y=20)

        self.entry_search = ttk.Entry(self)
        self.entry_search.place(x=105, y=20, width=150)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)
        btn_cancel.place(x=185, y=50)

        btn_search = ttk.Button(self, text="Поиск")
        btn_search.place(x=105, y=50)
        btn_search.bind('<Button-1>', lambda event: self.view.search_records(self.entry_search.get()))
        btn_search.bind('<Button-1>', lambda event: self.destroy(), add='+')


class DB:
    def __init__(self):
        with sq.connect('saper1.db') as self.con:
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users (
                kod INTEGER PRIMARY KEY AUTOINCREMENT,
                janr TEXT NOT NULL,
                strana TEXT NOT NULL,
                seria INTEGER,
                autor INTEGER,
                nazvanie TEXT NOT NULL,
                god INTEGER,
                anat TEXT NOT NULL
                )""")

    def insert_data(self, kod, janr, strana, seria, autor, nazvanie, god, anat):
        self.cur.execute(
            """INSERT INTO users(kod, janr, strana, seria, autor, nazvanie, god, anat) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (kod, janr, strana, seria, autor, nazvanie, god, anat))
        self.con.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Работа с базой данных Сапер")
    root.geometry("1050x600+300+200")
    root.resizable(False, False)
    root.mainloop()
