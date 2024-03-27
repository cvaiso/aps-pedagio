# this is the admin view class
# it handles the admin view
# we will be using tkinter for the view
import tkinter as tk
from tkinter import Menu
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from view.vehicle import VehicleView


class AdminView:
    def __init__(self, root):
        self.root = root
        self.root.title('Admin')
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
        # call control for the list of admins
        # for testing we will create a list of admins
        admins = [
            {
                'admin_name': 'admin1',
                'admin_email': 'email1',
                'admin_permission': 0
            },
            {
                'admin_name': 'admin2',
                'admin_email': 'email2',
                'admin_permission': 1
            },
            {
                'admin_name': 'admin3',
                'admin_email': 'email3',
                'admin_permission': 2
            }
        ]
        table_title_frame = tk.Frame(self.root)
        table_title_frame.grid(row=1, column=1)
        # I want to add a border to the table
        tk.Label(table_title_frame, text="Name", width=12, bg='white', relief='groove').pack(side='left')
        tk.Label(table_title_frame, text="Email", width=25, bg='white', relief='groove').pack(side='left')
        tk.Label(table_title_frame, text="Permission", width=12, bg='white',relief='groove').pack(side='left')

        table_content_frame = tk.Frame(self.root)
        table_content_frame.grid(row=2, column=1)

        # table frame
        for admin in admins:
            admin_frame = tk.Frame(table_content_frame, relief='groove')
            admin_frame.pack()
            tk.Label(admin_frame, text=admin['admin_name'], width=12, bg='light grey').pack(side='left')
            tk.Label(admin_frame, text=admin['admin_email'], width=25, bg='light grey').pack(side='left')
            tk.Label(admin_frame, text=admin['admin_permission'], width=12, bg='light grey').pack(side='left')
        

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