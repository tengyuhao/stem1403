"""
change or add element in a dictionary

if the keys exist in the dictionary, then it perform updating valur;

"""

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

# case 1.
# change January -> in french Janvier
months['Jan'] = "Janvier"
print(months)

# ex. change Feburay -> Fevrier
months['Feb'] = "Février"
print(months)

months['Mar'] = "Mars"
print(months)

# case 2.
months['Unknown'] = ['Unknowns-month']
print(months)

