
dict2_en = {
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thu": "Thursday",
    "fri": "Friday",
    "sat": "Saturday",
    "sun": "Sunday"
}

dict2_fr = {
    "mon": "Lundi",
    "tue": "Mardi",
    "wed": "Wednesday-fr",
    "thu": "Thursday-fr",
    "fri": "Friday-fr",
    "sat": "Saturday-fr",
    "sun": "Sunday-fr"
}


# example. i18h
# choose a language
print(dict2_en['mon'])
print(dict2_fr['mon'])
print()

# how to find out the french version for the identical key
for i in dict2_en:
    print(dict2_fr[i])

