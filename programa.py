#import psycopg2
import tkinter as tk
from view.login import LoginView
from view.admin import AdminView
from model.admin import Admin
from control.maincontrol import MainControl

#creating tkinter window
root = tk.Tk()
login = LoginView(root)
login.create_widgets()
root.mainloop()