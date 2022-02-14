"""
Hybrid 1
"""
class Car:
    def accelerate(self):
        pass

    def brake(self):
        pass

    def turn(self):
        pass


class ElectricCar(Car):
    def recharge(self):
        pass


class FuelCar(Car):
    def refill(self):
        pass


class HybridCar(ElectricCar, FuelCar):
    def switchmode(self):
        pass

