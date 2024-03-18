class Vehicle:
    def __init__(self, plate, model, color):
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
        self.owner = None
        # all cars have a value that indicates if its licensed, furted, etc
        self.status = "licensed"