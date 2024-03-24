# this is the admin view class
# it handles the admin view
# we will be using tkinter for the view
import tkinter as tk
from tkinter import Menu
from tkinter import Label
from tkinter import Entry
from tkinter import Button


class AdminView:
    def __init__(self, root):
        self.root = root
        self.root.title('Admin')
        self.root.geometry('1280x720')
        self.root.config(bg = 'light blue')
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        # we will have a menu bar with the following options
        # 1. Admin (add, delete, find)
        # 2. Tolloperator (add, delete, find)
        # 3. Tollbooth (add, delete, find)
        # 4. Vehicle (add, delete, find)
        # 5. Transaction (add, delete, find)
        menubar = Menu(self.root)
        adminmenu = Menu(menubar, tearoff=0)
        adminmenu.add_command(label="Add", command=self.add_admin)
        adminmenu.add_command(label="List", command=self.donothing)
        adminmenu.add_separator()
        adminmenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="Admin", menu=adminmenu)

        toperatormenu = Menu(menubar, tearoff=0)
        toperatormenu.add_command(label="Add", command=self.donothing)
        toperatormenu.add_command(label="List", command=self.donothing)
        menubar.add_cascade(label="Toll Operator", menu=toperatormenu)

        tollboothmenu = Menu(menubar, tearoff=0)
        tollboothmenu.add_command(label="Add", command=self.donothing)
        tollboothmenu.add_command(label="List", command=self.donothing)
        menubar.add_cascade(label="Toll Booth", menu=tollboothmenu)

        vehiclemenu = Menu(menubar, tearoff=0)
        vehiclemenu.add_command(label="Add", command=self.donothing)
        vehiclemenu.add_command(label="List", command=self.donothing)
        menubar.add_cascade(label="Vehicle", menu=vehiclemenu)

        transactionmenu = Menu(menubar, tearoff=0)
        transactionmenu.add_command(label="Analyse", command=self.donothing)
        menubar.add_cascade(label="Transaction", menu=transactionmenu)

        self.root.config(menu=menubar)

    def add_admin(self):
        # we will have a pop up windows
        # with the following fields
        # 1. Name
        # 2. Password
        # 3. Email
        # we will have a submit button
        # and a cancel button
        popup = tk.Toplevel(self.root)
        popup.title("Add Admin")
        popup.geometry('400x200')

        name_frame = tk.Frame(popup)
        name_frame.pack(anchor='center', expand=True)
        tk.Label(name_frame, text="Name").pack(side='left')
        tk.Entry(name_frame).pack(side='left')

        password_frame = tk.Frame(popup)
        password_frame.pack(anchor='center', expand=True)
        tk.Label(password_frame, text="Password").pack(side='left')
        tk.Entry(password_frame, show="*").pack(side='left')

        email_frame = tk.Frame(popup)
        email_frame.pack(anchor='center', expand=True)
        tk.Label(email_frame, text="Email").pack(side='left')
        tk.Entry(email_frame).pack(side='left')
    
        button_frame = tk.Frame(popup)
        button_frame.pack(anchor='center', expand=True)
        tk.Button(button_frame, text="Submit").pack(side='left')
        tk.Button(button_frame, text="Cancel", command=popup.destroy).pack(side='left')

    def donothing(self):
        pass