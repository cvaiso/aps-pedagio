import json
from model.admin import Admin
from model.vehicle import Vehicle
# this class is responsible for managing the data
# storing it in a json file, and reading it from the same file
# we will be storing a list of admins and a list of vehicles


class DataManager:
    def __init__(self):
        self.load_data()

    def load_data(self):
        try:
            with open('data/json_files/admins.json', 'r') as f:
                self.admins = [Admin.from_dict(data) for data in json.load(f)]
        except json.JSONDecodeError:
            self.admins = []
        try:
            with open('data/json_files/vehicles.json', 'r') as f:
                self.vehicles = [Vehicle.from_dict(data) for data in json.load(f)]
        except json.JSONDecodeError:
            self.vehicles = [] 
    
    # methods for admin
    def insert_admin(self, admin):
        self.admins.append(admin)

    def delete_admin(self, admin):
        for adm in self.admins:
            if adm.email == admin.email:
                self.admins.remove(adm)

    def find_admin(self, email):
        for admin in self.admins:
            if admin.email == email:
                return admin

    # methods for vehicle
    def insert_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    def delete_vehicle(self, vehicle):
        for veh in self.vehicles:
            if veh.plate == vehicle.plate:
                self.vehicles.remove(veh)
    def find_vehicle(self, plate):
        for vehicle in self.vehicles:
            if vehicle.plate == plate:
                return vehicle

    # method to close the data manager and save the data
    def close(self):
        with open('data/json_files/admins.json', 'w') as f:
            json.dump([admin.to_dict() for admin in self.admins], f)
        with open('data/json_files/vehicles.json', 'w') as f:
            json.dump([vehicle.to_dict() for vehicle in self.vehicles], f)