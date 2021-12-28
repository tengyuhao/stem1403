class Person:
    def __init__(self, name):
        self._name = name
        self._age = 1
        self._id = "ABCD12342123"

    def get_name(self):
        return self._name

    def set_name(self, newname):
        self._name = newname

    def get_id(self):
        return self._id

    def _print_id(self):
        pass

p1 = Person("Peter")
