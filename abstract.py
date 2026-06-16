from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand, speed):
        self.brand, self.speed = brand, speed

    @abstractmethod
    def fuel_type(self) -> str:
        pass

    @abstractmethod
    def start_engine(self) -> str:
        pass

    def vehicle_info(self):
        return f"{self.brand} | {self.fuel_type()} | " f"Top Speed: {self.speed} km/h"


class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric"

    def start_engine(self):
        return f"{self.brand}: Silent start"


Tesla = ElectricCar("Tesla", 250)

print(Tesla.start_engine())
print(Tesla.vehicle_info())
