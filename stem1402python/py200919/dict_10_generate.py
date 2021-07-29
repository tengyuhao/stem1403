"""
generate a dictionary
"""

"""
creating dictionary based on other dictionary
"""

# case 1. literal of dictionary
# dict()

my_dict = dict({1: 'apple', 2: 'orange'})
print(my_dict)

# case 2. compatible data structure

my_dict = dict([[3, 'apple'], [4, 'orange']])
print(my_dict)

# [[k,v],[k,v],[k,v]]
# # ((k,v),(k,v),(k,v),(k,v))
# [(k,v),(k,v),(k,v)]
# ([],[],[])