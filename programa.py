#import psycopg2
import tkinter as tk
from view.login import LoginView

class Programa:
#creating tkinter window
    def __init__(self):
        self.root = tk.Tk()
        self.login = LoginView(self.root)
        self.login.create_widgets()
    def run(self):
        self.root.mainloop()