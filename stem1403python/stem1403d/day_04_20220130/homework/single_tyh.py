
class Airplane:

    def __init__(self, name):
        self.name = name

    def fly(self):
        print("Airplane fly")


class MilitaryAirplane(Airplane):
    def shoot(self):
        print("Military Airplane shoot")

