"""
a dictionary of a dictionary

nested dictionary
"""

# a profile dataset of a company

"""
There is a campany who has a couple of employees
employee 1:
    empid:      001
    empfname:   Peter
    emplname:   White
    gender:     Male
    dob:        1990-09-01
    division:   Marketing
    salary:     5000
employee 2:
    empid:      002
    empfname:   Pierre
    emplname:   Antonio
    gender:     Male
    dob:        1992-05-02
    division:   Marketing
    salary:     4500
employee 3:
    empid:      003
    empfname:   Charls
    emplname:   Laporte
    gender:     Male
    dob:        1985-05-12
    division:   IT
    salary:     7000
"""

# selectproperkeys
company_profiles ={
    '001': {'empid': '001',
            'empfname': 'Peter',
            'emplname': 'White',
            'gender': 'Male',
            'dob': '1990-09-01',
            'division': 'Marketing',
            'salary': 5000},

    '002': {'empid': '002',
            'empfname': 'Pierre',
            'emplname': 'Antoniio',
            'gender': 'Male',
            'dob': '1992-05-02',
            'division': 'Marketing',
            'salary': 4500},

    '003': {'empid':'003',
            'empfname': 'Charls',
            'emplname': 'Laporte',
            'gender': 'Male',
            'dob': '1985-05-12',
            'division': 'IT',
            'salary': 7000}
}

profile1 = company_profiles['001']
print(profile1)
print(f"profile1['division'] : {profile1['division']} ")
print(f"profile1['salary'] : {profile1['salary']} ")
print()



profile2 = company_profiles['002']
print(profile2)
print(f"profile2['division'] : {profile2['division']} ")
print(f"profile2['salary'] : {profile2['salary']} ")
print()

profile3 = company_profiles['003']
print(profile3)
print(f"profile3['division'] : {profile3['division']} ")
print(f"profile3['salary'] : {profile3['salary']} ")
print()




