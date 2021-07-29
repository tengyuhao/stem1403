"""
variables arguments
"""


def foo1(x, y):
    print(x)
    print(y)

# TypeError: foo1() missing 1 required positional argument: 'y'
# foo1(1)


# TypeError: foo1() takes 2 positional arguments but 3 were given
# foo1(1, 2, 3)


def greeting(friend_name, words,):
    print(words, friend_name, "!")


friend_name1 = "Peter"
greeting(friend_name1, "Good morning,")

friend_name2 = "Mary"
greeting(friend_name2, "Good morning,")

friend_name3 = "Jackie"
greeting(friend_name3, "Good morning,")

