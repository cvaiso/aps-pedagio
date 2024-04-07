import tkinter as tk
from controller.login import LoginController
from view.admin import AdminView
from tkinter import messagebox

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry('1280x720')
        self.root.config(bg = 'light blue')
        self.root.resizable(False, False)
        self.create_widgets()
    def create_widgets(self):
        # we will have a login pagin with username and password
        # and a login and cancel button

        # username label and entry
        self.username_label = tk.Label(self.root, text = 'Email', bg = 'light blue')
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

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if LoginController.login(username, password) == True:
            print("Login bem sucedido!")
            # Adicione aqui o código para abrir a próxima tela do aplicativo após o login
            admin_window = tk.Toplevel(self.root)
            admin_view = AdminView(admin_window)
            self.root.withdraw()
        else:
            messagebox.showerror("Erro de login", "Usuário ou senha incorretos.")

    def cancel(self):
        pass