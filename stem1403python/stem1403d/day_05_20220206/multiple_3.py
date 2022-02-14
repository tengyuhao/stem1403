"""
multiple inherit
ver2
"""


class Father:
    def playmusic(self):
        print("classic")


class Mother:
    def playmusic(self):
        print("jazz")


class Child(Father, Mother):
    pass


class Child2(Mother, Father):
    pass


peter = Child()
peter.playmusic()
# peter.dance()

jack = Child2()
jack.playmusic()
# jack.dance()


