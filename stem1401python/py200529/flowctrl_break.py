"""

"""

# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     if i == 7:
#         break
#     print(i)

# break, jump out of current loop
# for i in [1, 2, 3, 4, 5]:
#     for j in [11, 22, 33, 44, 55]:
#         if j == 33:
#             break
#         print(i, j, end="\t")
#     print()


# break with while
i = 1
while True:
    print("i = ", i)
    i += 1
    if i > 10:
        break

# break, jump out of current loop
for i in [1, 2, 3, 4, 5]:
    for j in [11, 22, 33, 44, 55]:
        print(i, j, end="\t")
        if j == 33:
            break
    print()

