"""
variables arguments - arbitrary argument

*object
sep=" "
end="\n"


"""

# print()
# print(1)=
# print(1, 2)
# print(1, 2, "abc")

# print(*object, sep=" ", end="\n")


def greet(*friends):
    for name in friends:
        print(name)

    # print(friends, type(friends))


greet("Peter", "Marie", "Jackie", "Tony")
