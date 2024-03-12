class User:
    def __init__(self, name, ID, address, vehicle):
        """
        Initializes a new Vehicle object with the provided attributes.
        Args:
            name (str): The name of the user.
            ID (str): The ID of the user.
            address (str): The address of the user.
            vehicle (Vehicle): The vehicle of the user.
        """
        self.name = name
        self.ID = ID
        self.address = address
        self.vehicle = vehicle

    def __str__(self):
        """
        Returns:
            str: The string representation of the user.
        """
        return f"User: {self.name}, ID: {self.ID}, Address: {self.address}, Vehicle: {self.vehicle}"