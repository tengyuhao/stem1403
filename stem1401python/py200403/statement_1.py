"""
statement
object
variable
expression
"""

car = 10
print("car = ", car)

# multiple statements in one line
car = 10; print("car = ", car)

"""
//javascript
var car = 10;
console.leg("car = " + car);
"""

# One statement spans multiple lines ?
# case 1. using \

sum = 1 + 2 + 3 + 4 + \
    5 + 6 + 7 + 8

balance_jan = 1
balance_feb = 2
balance_mar = 3

balance_apr = 1
balance_may = 2
balance_jun = 3

# line 1: q1
# line 2: q2
# One statement
revenue = balance_jan + balance_feb + balance_mar + \
          balance_apr + balance_may + balance_jun

# Case 2. using brackets or similar symbols
a = (1 + 2 + 3 +
     4 + 5 + 6 +
     7 + 8 + 9)

colors = ['red',
          'blue',
          'green']
my_dictionary = {
  "a": 1,
  "b": 2
}
