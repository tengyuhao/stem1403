"""
access element from dictionary
1. []
2. get()

[] v.s. get()
"""

# case 1. []
months = {'Jan': 'January',
          'Feb': 'February',
          'Mar': 'March',
          'Apr': 'April',
          'May': 'May',
          'Jun': 'June',
          'Jul': 'July',
          'Aug': 'August',
          'Sep': 'September',
          'Oct': 'October',
          'Nov': 'November',
          'Dec': 'December'}

print(months['Jan'])

# case 2. get[]
key = 'Jan'
value = months.get(key)
print(f"Value of key:{key} is {value}.")

# KeyError: 'Unknown'
# result1 = months['Unknown']
# print(result1)

# return None
result2 = months.get("Unknown")
print(result2)

result2 = months.get("Unknown","unknown-key")
print(result2)

# how to use get()
if months.get("Unknown","unknown-key") == "unknown-key":
    pass






