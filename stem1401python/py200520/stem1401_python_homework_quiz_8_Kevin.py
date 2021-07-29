"""
Quiz 8
"""

# 8. Write a program to test if character ‘a’ or ‘A’ in a given sentence.
# Please output ‘True’ if there exists at least one ‘a’ or ‘A’,
# otherwise output ‘False’.

print("================== First Program ==================")

print("This is a program to test if character ‘a’ or ‘A’ in a given sentence")
a = input("Please input one string for test : ")

if 'a' in a:
    print(True)
else:
    if 'A' in a:
        print(True)
    else:
        print(False)
print("======================= End =======================")

# 9. Write a program to test if two lists with the same items are identical.
print("================= Second Program ==================")
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
list3 = [1, 2, 'a', 4, 5]
list4 = [1, 3, 6, 9]

print("list1 == list2? ", list1 == list2)
print("list1 == list3? ", list1 == list3)
print("list2 == list4? ", list2 == list4)

print("======================= End =======================")

# 10. Write a program to solve this problem.
# What is the day of week 100 days from now on?

"""
I don't understand this question and I don't know how to write this program.
"""
