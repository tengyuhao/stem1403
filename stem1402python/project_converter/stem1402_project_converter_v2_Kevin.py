"""
converter
"""


# functions ============================
def km_to_miles(kilometers_1):
    return kilometers_1 * 0.621371192


def miles_to_km(miles_2):
    return miles_2 / 0.621371192


def celsius_to_fahrenheit(cel_degree):
    return cel_degree * 1.8 + 32


def fahrenheit_to_celsius(fah_degree):
    return (fah_degree - 32) / 1.8


def kilogram_to_pound(kilogram_1):
    return kilogram_1 * 2.20462262


def pound_to_kilogram(pound_2):
    return pound_2 / 2.20462262


def meter_to_foot(s_meter):
    return s_meter / 0.09290304


def foot_to_meter(s_foot_2):
    return s_foot_2 * 0.09290304


def dollars_ca_to_yuan(dollars):
    return dollars / 0.19


def yuan_to_dollars_ca(yuan):
    return yuan * 5.15


def ml_to_l(ml):
    return ml / 1000


def l_to_ml(l):
    return l * 1000


# =========================================================================
print("Please choose a converter type:")
print("1. Length or Distance\n2. Temperature\n3. Weight or Mass\n4. Area\n5. Currency\n6. Capacity")
option_1 = int(input("Please enter the number of your choice: "))

if option_1 == 1:
    print("1. Kilometers To Miles\n2. Miles To Kilometers")
    option_2 = int(input("Please enter the number of your choice: "))

    if option_2 == 1:
        kilometers = float(input("Please enter a Kilometers to convert to Miles: "))
        print(f"{kilometers} kilometers = {km_to_miles(kilometers)} miles")

    elif option_2 == 2:
        miles = float(input("Please enter a Miles to covert to Kilometers: "))
        print(f"{miles} miles = {miles_to_km(miles)} kilometers")

    else:
        print("[Error] This number is error.")

elif option_1 == 2:
    print("1. Celsius To Fahrenheit\n2. Fahrenheit To celsius")
    option_2 = int(input("Please enter the number of your choice: "))

    if option_2 == 1:
        celsius = float(input("Please enter a degree Celsius to convert to Fahrenheit: "))
        print(f"{celsius}\u00B0C = {celsius_to_fahrenheit(celsius)}\u00B0F")

    elif option_2 == 2:
        fahrenheit = float(input("Please enter a degree Fahrenheit to convert to Celsius: "))
        print(f"{fahrenheit}\u00B0F = {fahrenheit_to_celsius(fahrenheit)}\u00B0C")

    else:
        print("[Error] This number is error!")

elif option_1 == 3:
    print("1. Kilogram To Pound\n2. Pound To Kilogram")
    option_2 = int(input("Please enter the number of your choice: "))

    if option_2 == 1:
        kilogram = float(input("Please enter a Kilograms to convert to Pounds: "))
        print(f"{kilogram} kilograms = {kilogram_to_pound(kilogram)} pounds")

    elif option_2 == 2:
        pound = float(input("Please enter a Pounds to convert to Kilograms: "))
        print(f"{pound} pounds = {pound_to_kilogram(pound)} kilograms")

    else:
        print("[Error] This number is error!")

elif option_1 == 4:
    print("1. Square meter To square foot\n2. Square foot To square meter")
    option_2 = int(input("Please enter the number of your choice: "))

    if option_2 == 1:
        square_meter = float(input("Please enter a Square meter to convert to Square foot: "))
        print(f"{square_meter} square meters = {meter_to_foot(square_meter)} square foots")

    elif option_2 == 2:
        square_foot = float(input("Please enter a Square foot to convert to Square meter: "))
        print(f"{square_foot} square foots = {foot_to_meter(square_foot)} square meters")

    else:
        print("[Error] This number is error!")

elif option_1 == 5:
    print("1. Canadian Dollars To Chinese Yuan\n2. Chinese Yuan To Canadian Dollars")
    option_2 = int(input("Please enter the number of your choice: "))

    if option_2 == 1:
        dollars = float(input("Please enter a Canadian Dollars to convert to Chinese Yuan: "))
        print(f"{dollars} Canadian Dollars = {dollars_ca_to_yuan(dollars)} Chinese Yuan")

    elif option_2 == 2:
        yuan = float(input("Please enter a Chinese Yuan to convert to Canadian Dollars: "))
        print(f"{yuan} Chinese Yuan = {yuan_to_dollars_ca(yuan)} Canadian Dollars")

    else:
        print("[Error] This number is error!")

elif option_1 == 6:
    print("1. Milliliter To Liter \n2. Liter To Milliliter")
    option_2 = int(input("Please enter the number of your choice: "))
    if option_2 == 1:
        ml = float(input("Please enter a Milliliter to convert to Liter: "))
        print(f"{ml} Milliliter = {ml_to_l(ml)} Liter")

    elif option_2 == 2:
        l = float(input("Please enter a Liter to convert to Milliliter: "))
        print(f"{l} Liter = {l_to_ml(l)} Milliliter")
    else:
        print("[Error] This number is error!")

else:
    print("[Error] This number is error.")

