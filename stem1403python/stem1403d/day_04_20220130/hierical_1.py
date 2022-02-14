
class Airplane:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print("Airplane fly")


class MilitaryAirplane(Airplane):
    def shoot(self):
        print("Military Airplane shoot")


class CivilAirplane(Airplane):
    def carry(self):
        print("Civil airplane carry the passengers")


class CargoAirplane(Airplane):
    def carry_merchandise(self):
        print("Cargo airplane carry the merchandise")

