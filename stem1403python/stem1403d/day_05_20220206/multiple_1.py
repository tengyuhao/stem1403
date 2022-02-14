"""
multiple inherit
vers 1
"""

class ParentB:
    pass

class ParentA:
    pass

class Child(ParentA, ParentB):
    pass