from project.vehicles.base_vehicle import BaseVehicle


class CargoVan(BaseVehicle):
    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, 180)

    def drive(self, mileage: float):
        percentage = round((mileage / 180) * 100) + 5
        self.battery_level -= percentage

