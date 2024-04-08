from data.datamanager import DataManager

class MainControl:
    data_manager = DataManager()

    @classmethod
    def get_next_admin_id(cls):
        return cls.data_manager.get_admin_id()

    @classmethod
    def add_admin(cls, admin):
        cls.data_manager.insert_admin(admin)

    @classmethod
    def remove_admin(cls, admin):
        cls.data_manager.delete_admin(admin)

    @classmethod
    def find_admin(cls, email):
        return cls.data_manager.find_admin(email)
    
    @classmethod
    def find_admin_by_name(cls, name):
        matching_admins = []
        for admin in cls.data_manager.admins:
            if admin.name == name:
                matching_admins.append(admin)
        return matching_admins
    
    @classmethod
    def get_all_admins(cls):
        return cls.data_manager.admins

    @classmethod
    def add_vehicle(cls, vehicle):
        cls.data_manager.insert_vehicle(vehicle)

    @classmethod
    def remove_vehicle(cls, vehicle):
        cls.data_manager.delete_vehicle(vehicle)

    @classmethod
    def find_vehicle(cls, plate):
        return cls.data_manager.find_vehicle(plate)
    
    @classmethod
    def get_all_vehicles(cls):
        return cls.data_manager.vehicles

    @classmethod
    def find_vehicle_by_model(cls, model):
        matching_vehicles = []
        for vehicle in cls.data_manager.vehicles:
            if vehicle.model == model:
                matching_vehicles.append(vehicle)
        return matching_vehicles
    
    @classmethod
    def login(cls, email, password):
        admin = cls.find_admin(email)
        if admin is not None:
            if admin.password == password:
                return admin
        return False

    @classmethod
    def close_data_manager(cls):
        cls.data_manager.close()