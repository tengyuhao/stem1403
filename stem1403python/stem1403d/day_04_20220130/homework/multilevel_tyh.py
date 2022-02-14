
class Airplane:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print("Airplane fly")


class CivilAirplane(Airplane):
    def carry(self):
        print("Civil airplane carry the passengers")


class AirCanada(CivilAirplane):
    def have(self):
        print("Air Canada have the Civil Airplane")
