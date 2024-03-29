from project.vehicles.base_vehicle import BaseVehicle


class PassengerCar(BaseVehicle):
    MAX_MILEAGE = 450.00

    def __init__(self, brand: str, model: str, license_plate_number: str):
        super().__init__(brand, model, license_plate_number, max_mileage=self.MAX_MILEAGE)

    def drive(self, mileage: float):
        percentage_to_subs = (mileage / self.MAX_MILEAGE) * 100
        self.battery_level -= round(percentage_to_subs)

# pc = PassengerCar("bmw", "m5", "asd")
# print(pc.drive(90))
# print(pc.battery_level)
