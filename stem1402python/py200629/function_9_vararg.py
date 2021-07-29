"""
function 9. variables arguments

default argument

rules:
positional arguments stay before all the default arguments
"""

# def greeting(words="Good morning," friend_name):
#     print(words, friend_name, "!")


def greeting(friend_name, words="Good morning,"):
    print(words, friend_name, "!")


# friend_name1 = "Peter"
# greeting(friend_name1)
#
# friend_name2 = "Mary"
# greeting(friend_name2)
#
# friend_name3 = "Jackie"
# greeting(friend_name3, "Good evening,")


def greeting(friendname="Marie", words="Good morning,"):
    print(words, friendname, "!")


greeting()

friend_name2 = "Lily"
greeting(friend_name2)

words2 = "Good afternoon,"
greeting(words=words2)

friend_name3 = "Jackie"
greeting(friend_name3, "Good evening,")

