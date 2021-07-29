"""
homework
"""
# 8. According the given syntax : print(*objects, sep=‘’, end=‘\n’, file=sys.stdout, flush=False)
# How can we output a 3X2 matrix and make the layout like 3 rows and 4 columns.
list1 = [[10, 11],
         [100, 110],
         [1000, 1100]]

print(list1[0][0], "\t\t", list1[0][1])
print(list1[1][0], "\t", list1[1][1])
print(list1[2][0], "\t", list1[2][1])

""" Sorry, I don't understand the question 9 """
# 9. Output the dimension of a box (width, height, depth) using a text template and format().
# 9.1 Input in the default order of width, height, depth
w1 = input("Please enter the width of the box: ")
h1 = input("Please enter the height of the box: ")
d1 = input("Please enter the depth of the box: ")
print("The dimension of the box is width: {}, height: {}, depth: {}".format(w1, h1, d1))
# Output Template:	The dimension of the box is width: 30cm, height: 20cm, depth: 10cm
# 9.2 Input in the order of width, height, depth
w2 = input("Please enter the width of the box: ")
h2 = input("Please enter the height of the box: ")
d2 = input("Please enter the depth of the box: ")
print("The dimension of the box is width: {}, height: {}, depth: {}".format(w2, h2, d2))

# Output Template:	The dimension of the box is width: 10cm, height: 20cm, depth: 30cm
# 9.3 Input in any order with named arguments
# Output Template:	The dimension of the box is width: 20cm, height: 30cm, depth: 10cm
w3 = input("Please enter the width of the box: ")
h3 = input("Please enter the height of the box: ")
d3 = input("Please enter the depth of the box: ")
print("The dimension of the box is width: {}, height: {}, depth: {}".format(w3, h3, d3))








