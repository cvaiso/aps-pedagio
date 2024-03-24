import psycopg2
import tkinter as tk
from view.login import LoginView
from view.admin import AdminView

# conn = psycopg2.connect(database = "pedagiodb", 
#                         user = "postgres", 
#                         host= 'localhost',
#                         password = "1234",
#                         port = 5432)

# # Open a cursor to perform database operations
# cur = conn.cursor()
# # Execute a command: create datacamp_courses table
# cur.execute("""CREATE TABLE admins(
#             admin_id SERIAL PRIMARY KEY,
#             admin_name VARCHAR (100) NOT NULL,
#             admin_password VARCHAR (20) NOT NULL,
#             admin_email VARCHAR (100) UNIQUE NOT NULL,
#             admin_permission INT NOT NULL,
#             admin_history TEXT []);
#             """)
# # Make the changes to the database persistent
# conn.commit()
# # Close cursor and communication with the database
# cur.close()
# conn.close()

#creating tkinter window
root = tk.Tk()
admin = AdminView(root)
# login = LoginView(root)
root.mainloop()