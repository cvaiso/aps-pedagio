class User:
    def __init__(self, name, CPF, vehicle):
        """
        Initializes a new Vehicle object with the provided attributes.
        Args:
            name (str): The name of the user.
            ID (str): The ID of the user.
            address (str): The address of the user.
            vehicle (Vehicle): The vehicle of the user.
        """
        self.name = name
        self.CPF = CPF
        self.status = "licensed"

    def __str__(self):
        """
        Returns:
            str: The string representation of the user.
        """
        return f"User: {self.name}, ID: {self.ID}, Address: {self.address}, Vehicle: {self.vehicle}"