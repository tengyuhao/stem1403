"""

"""


class House:
    def __init__(self, typeH, area):
        self.typeH = typeH
        self.area = area
        self.listF = []
        self.free_area = area

    def valid(self):
        if Furniture.addItem() == 0:
            print("The space is all")
        else:
            self.addItem()

    def addItem(self, houseItem):

        self.listF.addItem(houseItem)

        self.freearea = self.area - self.area

    def __str__(self):
        return f"Type of home: {self.typeH}, Free Area finally:{self.addItem()}, list: {self.list}"


class Furniture:
    def __init__(self, name, area):
        self.name = name
        self.area = area


    def __str__(self):
        return f"Object: {self.typeH}, Area used:{self.addItem()}"

