import tkinter as tk
#import AdminView from view/admin
from view.admin import AdminView

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry('1280x720')
        self.root.config(bg = 'light blue')
        self.root.resizable(False, False)
    def create_widgets(self):
        # we will have a login pagin with username and password
        # and a login and cancel button

        # username label and entry
        self.username_label = tk.Label(self.root, text = 'Username', bg = 'light blue')
        self.username_label.place(x = 500, y = 250)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.place(x = 600, y = 250)

        # password label and entry
        self.password_label = tk.Label(self.root, text = 'Password', bg = 'light blue')
        self.password_label.place(x = 500, y = 300)
        self.password_entry = tk.Entry(self.root, show = '*')
        self.password_entry.place(x = 600, y = 300)

        # login button
        self.login_button = tk.Button(self.root, text = 'Login', bg = 'light grey', command = self.login)
        self.login_button.place(x = 650, y = 350)

        # cancel button
        self.cancel_button = tk.Button(self.root, text = 'Cancel', bg = 'light grey', command = self.root.quit)
        self.cancel_button.place(x = 550, y = 350)
    # the clear method will clear the root window, so that we can use it for the admin view
    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    def login(self):
        # call control to check if the user is in the database
        # if the user is in the database, check if it is an admin
        # if it is an admin, call the admin view
        admin = AdminView(self.root)
        self.clear()
        admin.create_widgets()