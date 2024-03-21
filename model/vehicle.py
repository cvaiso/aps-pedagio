class Vehicle:
    def __init__(self, plate, model, color, status = "licensed"):
        """
        Initializes a new Vehicle object with the provided attributes.
        Args:
            plate (str): The plate of the vehicle.
            model (str): The model of the vehicle.
            color (str): The color of the vehicle.
        """
        self.plate = plate
        self.model = model
        self.color = color
        self.status = status
    
    def __str__(self):
        return f"Vehicle: {self.plate}, Model: {self.model}, Color: {self.color}, Status: {self.status}"
    