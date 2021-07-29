"""
join()
returns a string by joining all the elements of an iterable,
separated by a string separator.
string.join(iterable)
iterable = list, tuple, set, dictionary, string
"""
# Example 1. list
mylist1 = ['a','b','c', '1', '2', '3']
sep = ','
result = sep.join(mylist1)
print(result, type(result))
mylist1 = ['Python','is','an', 'awesome', 'programming', 'language']
sep = ' '
result = sep.join(mylist1)
print(result, type(result))
sep = ''
result = sep.join(mylist1)
print(result, type(result))
print("=========\n")
# Example 2. tuple
mytuple1 = ('a','b','c', '1', '2', '3')
sep = ' '
result = sep.join(mytuple1)
print(result, type(result))
print("=========\n")
# Example 3. set
myset1 = {'a','b','c', '1', '2', '3'}
sep = ' '
result = sep.join(myset1)
print(result, type(result))
myset2 = {'a','b','c', '1', '2', '3'}
sep = ''
result = sep.join(myset2)
print(result, type(result))
print("=========\n")
# Example 4.
s1 = 'abc'
s2 = '123'
print('s1.join(s2):', s1.join(s2))
s1 = '123'
s2 = 'abc'
print('s1.join(s2):', s1.join(s2))
print("=========\n")
# Example 5. dictionary
mydict = {'m':'monday', 't':'tuesday'}
sep = ','
print(sep.join(mydict))
# error
# mydict = {1:'monday', 2:'tuesday'}
# sep = ','
# print(sep.join(mydict))
mydict = {'1':'monday', '2':'tuesday'}
sep = ','
print(sep.join(mydict))