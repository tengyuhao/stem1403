"""

"""


class GrandParent:
    def __init__(self):
        print("GrandParent __init__() called.")


class Son(GrandParent):
    pass


class GrandSon(Son):
    pass
