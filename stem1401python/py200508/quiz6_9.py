"""

"""

width = 30
height = 20
depth = 10

# 9.1
temp1 = "The dimension of the box is: width {}cm, height {}cm, depth {}cm"
print(temp1.format(width, height, depth))

# 9.2
temp2 = "The dimension of the box is: depth {2}cm, height {1}cm, width {0}cm"
print(temp2.format(width, height, depth))

# 9.3
temp3 = "The dimension of the box is: height {h}cm, depth {d}cm, width {w}cm"
print(temp3.format(w=width, h=height, d=depth))