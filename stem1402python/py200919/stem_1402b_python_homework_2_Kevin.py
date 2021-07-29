"""
1. Write a Python program to generate and print a dictionary that contains a number (between 1 and n)
in the form (x, x*x).
e.g. User inputs 5
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
2. Write a program to concatenate following dictionaries to create a new one.
Sample Dictionary :
dict1={1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
3. Please remove the items with a key of integer type from the given dictionary and print out the new dictionary.
The given dictionary is as following:
person_profile = {
    'empid': '0001',
    'name': 'Peter',
    'ismanager': True,
    1: 'availabe',
    2: 'long-term'
}
"""

# 1.
print("Question 1.")
num = int(input("Please enter one numbers: "))
dict1 = {}
for i in range(1, num+1):
    # print(i)
    i2 = i * i
    # i2 = str(i2)
    dict1[i] = i2
print(dict1)

print()

# 2.
print("Question 2.")

dict2={1:10, 2:20}
dict3={3:30, 4:40}
dict4={5:50,6:60}


dict2.update(dict3)
dict3.update(dict4)
print(dict1)

print()

# 3.
print("Question 3.")
person_profile = {
    'empid': '0001',
    'name': 'Peter',
    'ismanager': True,
    1: 'availabe',
    2: 'long-term'
}

for i in person_profile:
    if not isinstance(i, int):
        person_profile.pop(i)


print(person_profile)








