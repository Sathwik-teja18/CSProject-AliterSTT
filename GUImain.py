#!!This program is still a work in progress!!

import tkinter as tk
import mysql.connector


class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MainWindow")
        self.geometry('900x700')
        self.B1=tk.Button(text="Admin", padx=50, pady=20, command=self.Admin)
        self.B2=tk.Button(text="Buyer", padx=50, pady=20, command=self.Buyer)
        self.B2.pack()
        self.B1.pack()
        self.mainloop()

    def Admin(self):
        self.B1.forget()
        self.B2.forget()
        self.title("Admin")
        self.geometry('500x300')
        self.l1=tk.Label(text="Enter Password")
        self.e1=tk.Entry()
        self.l1.pack()
        self.e1.pack()
        self.mainloop()

    def Buyer(self):
        self.B1.forget()
        self.B2.forget()
        self.title("Buyer")
        self.geometry('900x700')
        self.BB1=tk.Button(text="View Items", padx=50, pady=20, command=self.BList)
        self.BB1.pack()

    def BList(self):
        self.BB1.forget()
        try:
            self.db=mysql.connector.connect(user='root', password='', host='localhost', database='SHOP')
            self.cu=self.db.cursor()
            self.Q="SELECT * FROM GROCCERIES"
            self.cu.execute(self.Q)
            self.data=self.cu.fetchall()
            print(self.data)
        except  mysql.connector.Error as err:
            print(f"Error {err}")


Gui()
