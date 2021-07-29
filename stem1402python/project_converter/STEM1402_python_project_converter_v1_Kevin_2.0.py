"""
converter
"""


# functions ============================
def km_to_miles(kilometers_1):
    miles_1 = kilometers_1 * 0.621371192
    return miles_1


def miles_to_km(miles_2):
    kilometers_2 = miles_2 / 0.621371192
    return kilometers_2


def celsius_to_fahrenheit(cel_degree):
    fahrenheit_1 = cel_degree * 1.8 + 32
    return fahrenheit_1


def fahrenheit_to_celsius(fah_degree):
    celsius_2 = (fah_degree - 32) / 1.8
    return celsius_2


def kilogram_to_pound(kilogram_1):
    pound_1 = kilogram_1 * 2.20462262
    return pound_1


def pound_to_kilogram(pound_2):
    kilogram_2 = pound_2 / 2.20462262
    return kilogram_2


def meter_to_foot(s_meter):
    s_foot = s_meter / 0.09290304
    return s_foot


def foot_to_meter(s_foot_2):
    s_meter_2 = s_foot_2 * 0.09290304
    return s_meter_2


# =========================================================================
print("Please choose a converter type:")
print("1. Length or Distance\n2. Temperature\n3. Weight or Mass\n4. Area")
option_1 = float(input("Please enter the number of your choice: "))

if option_1 == 1:
    print("1. Kilometers To Miles\n2. Miles To Kilometers")
    option_2 = float(input("Please enter the number of your choice: "))

    if option_2 == 1.0:
        kilometers = float(input("Please enter a Kilometers to convert to Miles: "))
        print(f"{kilometers} kilometers = {km_to_miles(kilometers)} miles")

    elif option_2 == 2.0:
        miles = float(input("Please enter a Miles to covert to Kilometers: "))
        print(f"{miles} miles = {miles_to_km(miles)} kilometers")

    else:
        print("[Error] This number is error.")

elif option_1 == 2:
    print("1. Celsius To Fahrenheit\n2. Fahrenheit To celsius")
    option_2 = float(input("Please enter the number of your choice: "))

    if option_2 == 1.0:
        celsius = float(input("Please enter a degree Celsius to convert to Fahrenheit: "))
        print(f"{celsius}\u00B0C = {celsius_to_fahrenheit(celsius)}\u00B0F")

    elif option_2 == 2.0:
        fahrenheit = float(input("Please enter a degree Fahrenheit to convert to Celsius: "))
        print(f"{fahrenheit}\u00B0F = {fahrenheit_to_celsius(fahrenheit)}\u00B0C")

    else:
        print("[Error] This number is error!")

elif option_1 == 3:
    print("1. Kilogram To Pound\n2. Pound To Kilogram")
    option_2 = float(input("Please enter the number of your choice: "))

    if option_2 == 1.0:
        kilogram = float(input("Please enter a Kilograms to convert to Pounds: "))
        print(f"{kilogram} kilograms = {kilogram_to_pound(kilogram)} pounds")

    elif option_2 == 2.0:
        pound = float(input("Please enter a Pounds to convert to Kilograms: "))
        print(f"{pound} pounds = {pound_to_kilogram(pound)} kilograms")

    else:
        print("[Error] This number is error!")

elif option_1 == 4:
    print("1. Square meter To square foot\n2. Square foot To square meter")
    option_2 = float(input("Please enter the number of your choice: "))

    if option_2 == 1.0:
        square_meter = float(input("Please enter a Square meter to convert to Square foot: "))
        print(f"{square_meter} square meters = {meter_to_foot(square_meter)} square foots")

    elif option_2 == 2.0:
        square_foot = float(input("Please enter a Square foot to convert to Square meter: "))
        print(f"{square_foot} square foots = {foot_to_meter(square_foot)} square meters")

    else:
        print("[Error] This number is error!")

else:
    print("[Error] This number is error.")

