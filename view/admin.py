# this is the admin view class
# it handles the admin view
# we will be using tkinter for the view
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from view.vehicle import VehicleView
from model.admin import Admin


class AdminView:
    def __init__(self, root):
        self.root = root
        self.root.title('Admin')
        self.vehicle = None
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
        adminmenu.add_command(label="List", command=self.list_admin)
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
        vehiclemenu.add_command(label="Add", command=self.add_vehicle)
        vehiclemenu.add_command(label="List", command=self.donothing)
        menubar.add_cascade(label="Vehicle", menu=vehiclemenu)

        transactionmenu = Menu(menubar, tearoff=0)
        transactionmenu.add_command(label="Analyse", command=self.donothing)
        menubar.add_cascade(label="Transaction", menu=transactionmenu)

        self.root.config(menu=menubar)
    def add_admin(self):
        # we need to check te admin permission, if it is 0
        # we will not allow the admin to add another admin

        # we will have a pop up windows
        # with the following fields
        # 1. Name
        # 2. Password
        # 3. Email
        # 4. Permission
        # we will have a submit button
        # and a cancel button
        popup = tk.Toplevel(self.root)
        popup.title("Add Admin")
        popup.geometry('300x400')
        popup.configure(bg='light blue')

        name_frame = tk.Frame(popup)
        name_frame.pack(anchor='w', expand=True)
        tk.Label(name_frame, text="Name", width=12, bg='light blue').pack(side='left')
        tk.Entry(name_frame, width=25).pack(side='left')

        password_frame = tk.Frame(popup)
        password_frame.pack(anchor='w', expand=True)
        tk.Label(password_frame, text="Password", width=12, bg='light blue').pack(side='left')
        tk.Entry(password_frame, show="*", width=25).pack(side='left')

        email_frame = tk.Frame(popup)
        email_frame.pack(anchor='w', expand=True)
        tk.Label(email_frame, text="Email", width=12, bg='light blue').pack(side='left')
        tk.Entry(email_frame, width=25).pack(side='left')

        permission_frame = tk.Frame(popup)
        permission_frame.pack(anchor='w', expand=True)
        tk.Label(permission_frame, text="Permission", width=12, bg='light blue').pack(side='left')
        permission_entry = tk.Entry(permission_frame, width=25)
        permission_entry.insert(0, "0")
        permission_entry.pack(side='left')

        button_frame = tk.Frame(popup)
        button_frame.pack(anchor='center', expand=True)
        tk.Button(button_frame, text="Submit").pack(side='left')
        tk.Button(button_frame, text="Cancel", command=popup.destroy).pack(side='left')
    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_widgets()
    def list_admin(self):
        # we will have a list of admins
        # with the following fields
        # 1. Name
        # 2. Email
        # 3. Permission
        # 4. History
        # we will have a search bar
        # and a search button
        # we will have a delete button
        # we will show the admins from a list of admins
        # it will be shown in the same window

        # table frame
        self.clear()
        # creating fake data to test the view
        admins = []
        for i in range(50):
            admins.append(Admin("John Doe", "1234", "email1@test.com"))
        # making every grid have a minimum size
        self.root.grid_rowconfigure(0, minsize=100)
        self.root.grid_columnconfigure(0, minsize=100)
        # table label
        table_label = Label(self.root)
        # creating tree
        tree = ttk.Treeview(table_label)
        # defining columns
        tree["columns"] = ("Name", "Email", "Permission")
        # format columns
        tree.column("#0", width=0, stretch=tk.NO)
        tree.column("Name", anchor=tk.W, width=200)
        tree.column("Email", anchor=tk.CENTER, width=200)
        tree.column("Permission", anchor=tk.CENTER, width=80)
        # creaing headings
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("Name", text="Name", anchor=tk.CENTER)
        tree.heading("Email", text="Email", anchor=tk.CENTER)
        tree.heading("Permission", text="Permission", anchor=tk.CENTER)
        # adding the fake data
        for i, admin in enumerate(admins):
            tree.insert(parent="", index=tk.END, iid=i, text="", values=(admin.name, admin.email, admin.permission))
        # placing tree
        tree.pack()
        # placing the table label
        table_label.grid(row=1, column=1, rowspan=4, columnspan=4, padx=10, pady=10)
        # label for search bar
        search_label = Label(self.root)
        # placing search label
        search_label.grid(row=1, column=7, padx=10, sticky='s')
        name_label = Label(search_label, text="Name").grid(row=0, column=0)
        email_label = Label(search_label, text="Email").grid(row=0, column=1)
        # entry boxes for search bar
        name_entry = Entry(search_label, width=30).grid(row=1, column=0)
        email_entry = Entry(search_label, width=30).grid(row=1, column=1)
        # creating an empty label to create space
        empty_label = Label(self.root, width=20, bg='light blue')
        empty_label.grid(row=1, column=6)

        # creating buttons
        button_search = Button(self.root, text="Search")
        button_search.grid(row=2, column=7, padx=10)
        # label for remove buttons
        remove_label = Label(self.root, bg='light blue')
        button_remove_one = Button(remove_label, text="Remove One")
        button_remove_one.pack(side='left', padx=10)
        button_remove_many = Button(remove_label, text="Remove Many")
        button_remove_many.pack(side='left', padx=10)
        remove_label.grid(row=6, column=2, padx=10, columnspan=2)





    def add_vehicle(self): 
        if self.vehicle is None:
            self.vehicle = VehicleView(self.root)
        self.vehicle.add_vehicle()
    def list_vehicle(self):
        # create a vehicle view object if it does not exist
        if self.vehicle is None:
            self.vehicle = VehicleView(self.root)
        self.vehicle.list_vehicle()
    def donothing(self):
        pass