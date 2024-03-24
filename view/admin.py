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
    
    def add_vehicle(self):
        # we will have a pop up windows
        # with the following fields
        # 1. Plate
        # 2. Model
        # 3. Color
        # 4. Status
        # we will have a submit button
        # and a cancel button

        popup = tk.Toplevel(self.root)
        popup.title("Add Vehicle")
        popup.geometry('300x400')
        popup.configure(bg='light blue')

        plate_frame = tk.Frame(popup)
        plate_frame.pack(anchor='w', expand=True)
        tk.Label(plate_frame, text="Plate", width=12, bg='light blue').pack(side='left')
        tk.Entry(plate_frame, width=25).pack(side='left')

        model_frame = tk.Frame(popup)
        model_frame.pack(anchor='w', expand=True)
        tk.Label(model_frame, text="Model", width=12, bg='light blue').pack(side='left')
        tk.Entry(model_frame, width=25).pack(side='left')

        color_frame = tk.Frame(popup)
        color_frame.pack(anchor='w', expand=True)
        tk.Label(color_frame, text="Color", width=12, bg='light blue').pack(side='left')
        tk.Entry(color_frame, width=25).pack(side='left')

        status_frame = tk.Frame(popup)
        status_frame.pack(anchor='w', expand=True)
        tk.Label(status_frame, text="Status", width=12, bg='light blue').pack(side='left')
        status_entry = tk.Entry(status_frame, width=25)
        status_entry.insert(0, "licensed")
        status_entry.pack(side='left')

        button_frame = tk.Frame(popup)
        button_frame.pack(anchor='center', expand=True)
        tk.Button(button_frame, text="Submit").pack(side='left')
        tk.Button(button_frame, text="Cancel", command=popup.destroy).pack(side='left')
    
    def list_vehicle(self):
        # we wil list all the vehicle in the database
        # and allow the user to order then by plate, model, color or status
        # we will have a search bar to find a vehicle by plate
        # we will have a delete button to delete a vehicle

        # we will have a table with the following columns
        # 1. Plate
        # 2. Model
        # 3. Color
        # 4. Status

        # we will have a search bar to find a vehicle by plate placed right the table
        # we will have a delete button to delete a selected vehicle placed right the table

    def donothing(self):
        pass