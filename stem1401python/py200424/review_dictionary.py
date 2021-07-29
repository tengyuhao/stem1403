"""
/Users/kevinteng/PycharmProjects/stem1401python/py200424/review_dictionary.py
"""
birthday_friends_mm_dd = {
    "Dave": "Feb_09",
    "Francis": "Aug_30",
    "Luke": "May_04"
}
# DoB, Last Name, School, City
my_friends = {
    "Dave": ("Feb_09", "White", "ABC High School", "Montreal"),
    "Francis": ("Aug_30", "Brian", "BBA High School","Paris"),
    "Luke": ("May_04", "Regon", "CCC High School","Toronto")
}
# print out info of Dave
print(my_friends["Dave"], type(my_friends["Dave"]))

# print out the City where Dave lives at
print(my_friends["Dave"][3])
