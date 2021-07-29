"""
[Homework]
1. Map two lists into a dictionary for day of week
list1 = ['MON','TUE','WED','THU','FRI','SAT','SUN']
list2 = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
2. Create a dictionary properly and sorting by age in ascending order, then sorting by score in descending order.
Both results are required to print out.
name   age    score
Amy    22     92
Lily   24     100
Sandy  21     87
Peter  23     96
Jack   22     94
3. There are 3 candidates in the election for President in ABC country.
They got voted in every state/province in ABC country.
You are asked to calculate who got the highest vote in the election.
Name      Voted in State1       Voted in State2     Voted in State3
Jason     300                   360                 270
Bill      280                   340                 291
William       350               310                 324
"""

# Question 1.
print("Question 1.")
list1 = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
list2 = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
mydict = dict(zip(list1, list2))
print(mydict)

# Question 2.
print("Question 2.")
"""
name   age    score
Amy    22     92
Lily   24     100
Sandy  21     87
Peter  23     96
Jack   22     94
"""

age_student = {
    "Amy": 22,
    "Lily": 24,
    "Sandy": 21,
    "Peter": 23,
    "Jack": 22
}

score_student = {
    "Amy": 92,
    "Lily": 100,
    "Sandy": 87,
    "Peter": 96,
    "Jack": 94
}

import operator

sorted_age_student = dict(sorted(age_student.items(), key=operator.itemgetter(1)))
print("Student's age in ascending order", sorted_age_student)

sorted_score_student = dict(sorted(score_student.items(), key=operator.itemgetter(1), reverse=True))
print("Student's score in descending order", sorted_score_student)

# Question 3.
print("Question 3. ")

"""
Name      Voted in State1       Voted in State2     Voted in State3
Jason     300                   360                 270
Bill      280                   340                 291
William       350               310                 324
"""

from collections import Counter
# data from state 1
vote_state1 = {
    "Jason": 300,
    "Bill": 280,
    "William": 350
}

# data from state 2
vote_state2 = {
    "Jason": 360,
    "Bill": 340,
    "William": 310
}

# data from state 3
vote_state3 = {
    "Jason": 270,
    "Bill": 291,
    "William": 324
}

res = Counter(vote_state1) + Counter(vote_state2) + Counter(vote_state3)
print(res)
result = max(res)
print(result)


