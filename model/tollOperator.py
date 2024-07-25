class TollOperator:
    def __init__(self, operatorid, name, email, password):
        self.operatorid = operatorid
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"Operator ID: {self.operatorid}, Name: {self.name}, Email: {self.email}, Password: {self.password}"

    def to_dict(self):
        return {
            'operatorid': self.operatorid,
            'name': self.name,
            'email': self.email,
            'password': self.password,
        }
    
    @classmethod
    def from_dict(cls, data):
        tollOperator = cls(data['operatorid'], data['name'], data['email'], data['password']) 
        return tollOperator