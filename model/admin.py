class Admin:
    id = 100000
    def __init__(self, name, password, email, permission = 1):
        self.id = id+0    
        self.name = name
        self.password = password
        self.email = email


        self.permission = permission
        self.history = []
    def __str__(self):
        return f"Admin: {self.name}, Email: {self.email}, Permission: {self.permission}"