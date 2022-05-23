"""
class member: static method
"""

class MyFormatter:

    count_sep = 0

    @staticmethod
    def showTitle():
        print("========================")
        print("===    My Plotter    ===")
        print("=== Starter  Edition ===")

    @staticmethod
    def printSeparator(mychar='*'):
        print(mychar*20)
        MyFormatter.countSeparator()

    @staticmethod
    def showFooter():
        print("==== Footer ====")

    @classmethod
    def countSeparator(cls):
        cls.count_sep += 1

# test and use
# main logic
MyFormatter.showTitle()
print("content 1")
print("content 2")
print("content 3")
print("content 4")
MyFormatter.printSeparator()
print("content 1")
print("content 2")
print("content 3")
print("content 4")
MyFormatter.printSeparator()
print("content 1")
print("content 2")
print("content 3")
print("content 4")
MyFormatter.printSeparator()
print("content 1")
print("content 2")
print("content 3")
print("content 4")
MyFormatter.printSeparator()
MyFormatter.showFooter()

print()
print(f"You have drawn {MyFormatter.count_sep} separators")