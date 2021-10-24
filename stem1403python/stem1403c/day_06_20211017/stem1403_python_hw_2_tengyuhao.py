"""
project: PvZ
plant module
"""


class Plant:
    pass


class PotatoMine:
    def __init__(self, name, color, hp, height):
        self.name = name
        self.color = color
        self.hp = hp
        self.height = height

    #  adding methods
    def explode(self):
        pass


class Sunflower:
    def __init__(self, name, color, hp, height):
        self.name = name
        self.color = color
        self.hp = hp
        self.height = height

    #  adding methods
    def provide(self):
        pass


class Wallnut:
    def __init__(self, name, color, hp, height):
        self.name = name
        self.color = color
        self.hp = hp
        self.height = height

    #  adding methods
    def block(self):
        pass


class ShowPea:
    def __init__(self, name, color, hp, height, shot_distance):
        self.name = name
        self.color = color
        self.hp = hp
        self.height = height
        self.shot_distance = shot_distance

    #  adding methods
    def shoot(self):
        pass
