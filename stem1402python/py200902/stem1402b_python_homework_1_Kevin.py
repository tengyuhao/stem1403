"""
1. Define a python dictionary to represent a real thing in the world.
e.g. Day of week
2. Access every item in the dictionary defined by you in Question 1 by iteration.
Print out necessary information in proper layout.
3. Define a nested dictionary to represent a real thing in the world. Choose proper keys.
e.g. Employ profile
4. Access the item (entry) in the dictionary defined by you in Question 3 by specified key.
The key should be input by users. Print out necessary information in proper layout.
"""

# 1.
print("Question 1.")
commision_scolaire_montreal = {'CSSDM': 'Centre de services scolaire de Montréal',
                      'CSSPI': 'Centre de services scolaire de la Pointe-de-l\'île',
                      'CSSMB': 'Centre de services scolaire Marguerite- Bourgeoys',
                      'LBPSB': 'Commission scolaire Lester-B.-Pearson',
                      'CSEM': 'Commission scolaire English-Montreal'
}

# 2
for i in commision_scolaire_montreal:
    print(f"{i}'s full name is {commision_scolaire_montreal[i]}")

# 3
groups_profils = {
    '1601':
    {
        'groupeid': '1601',
        "number_students": "29",
        "french_teacher": "Francis",
        "math_teacher": "Pierre",
        "english_teacher": "Amanda",
        "grade": "6e_primary"
    },

    '2101':
    {
        'groupeid': '2101',
        "number_students": "32",
        "french_teacher": "Francine",
        "math_teacher": "Antonin",
        "english_teacher": "Diane",
        "history_teacher": "Anne",
        "grade": "1e_sec"
    },

    '2301':
    {
        'groupeid': '2301',
        "number_students": "35",
        "french_teacher": "Francine",
        "math_teacher": "Stanly",
        "english_teacher": "Diane",
        "history_teacher": "Vincent",
        "sport_teacher": "Peter",
        "grade": "3e_sec"
    }
}

# 4.
print("Question 4.")
print("If you want to information for group: 1601, please type 1601.")
print("If you want to information for group: 2101, please type 2101.")
print("If you want to information for group: 2301, please type 2301.")
groupid = input("Now, please enter the group number to see: ")

if groupid == "1601":
    print(groups_profils['1601'])
elif groupid == "2101":
    print(groups_profils['2101'])
elif groupid == "2301":
    print(groups_profils['2301'])