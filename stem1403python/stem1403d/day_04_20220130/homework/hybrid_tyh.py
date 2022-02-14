"""

"""


class School:
    def __init__(self, name):
        self.name = name


class Exam(School):
     def print(self):
         print("Print exam")


class Teacher(School):
    def teach(self):
        print("Teacher teach")


class Student(Exam, School):
    pass

