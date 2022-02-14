"""

"""


class Train:
    def __init__(self, name):
        self.name = name

    def run(self):
        print("Train run")


class Airplane:
    def __init__(self, name):
        self.name = name

    def fly(self):
        print("Airplane fly")


class Transportation(Train, Airplane):
    pass
