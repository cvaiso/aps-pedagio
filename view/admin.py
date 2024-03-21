# this is the admin view class
# it handles the admin view
# we will be using tkinter for the view
import tkinter as tk
from tkinter import Menu


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
        adminmenu.add_command(label="Add", command=self.donothing)
        adminmenu.add_command(label="Delete", command=self.donothing)
        adminmenu.add_command(label="Find", command=self.donothing)
        adminmenu.add_separator()
        adminmenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="Admin", menu=adminmenu)

        self.root.config(menu=menubar)
        self.root.mainloop()
    def donothing(self):
        pass