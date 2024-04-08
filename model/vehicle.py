class Vehicle:
    def __init__(self, plate, model, color, status = "licensed"):
        self.plate = plate
        self.model = model
        self.color = color
        self.status = status
    
    def __str__(self):
        return f"Vehicle: {self.plate}, Model: {self.model}, Color: {self.color}, Status: {self.status}"

    def to_dict(self):
        return {
            'plate': self.plate,
            'model': self.model,
            'color': self.color,
            'status': self.status
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['plate'], data['model'], data['color'], data.get('status', 'licensed')) 