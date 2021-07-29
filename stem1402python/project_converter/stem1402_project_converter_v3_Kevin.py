"""
converter
"""


# functions ============================
def km_to_miles(km):
    return km * 0.621371192


def miles_to_km(miles):
    return miles / 0.621371192


def cm_to_m(cm):
    return cm / 100


def m_to_cm(m):
    return m * 100


def celsius_to_fahrenheit(cel_degree):
    return cel_degree * 1.8 + 32


def fahrenheit_to_celsius(fah_degree):
    return (fah_degree - 32) / 1.8


def kilogram_to_pound(kg):
    return kg * 2.20462262


def pound_to_kilogram(pound):
    return pound / 2.20462262


def kilogram_to_gram(kg):
    return kg * 1000


def gram_to_kilogram(g):
    return g / 1000


def meter_to_foot(s_meter):
    return s_meter / 0.09290304


def foot_to_meter(s_foot):
    return s_foot * 0.09290304


def dollars_ca_to_yuan(dollar):
    return dollar / 0.19


def yuan_to_dollars_ca(yuan):
    return yuan * 5.15


def dollars_ca_to_gbp(dollar):
    return dollar * 1.70


def gbp_to_dollars_ca(dollar):
    return dollar * 1.70


def ml_to_l(ml):
    return ml / 1000


def l_to_ml(l):
    return l * 1000


# =========================================================================
print("=================== Welcome to this program! My mini converter ===================")
while True:
    print("")
    print("Please choose a converter type:")
    print("0. Exit to the program\n1. Length or Distance\n2. Temperature\n3. Weight or Mass\n4. Area\n5. Currency"
          "\n6. Capacity")
    option_1 = int(input("Please enter the number of your choice: "))

    print()

    if option_1 == 0:
        print("Goodbye! See you next time.")
        break

    elif option_1 == 1:
        while True:
            print("0: Exit this section.")
            print("1. Kilometers To Miles\n2. Miles To Kilometers")
            print("3. Centimeters To Meters\n4. Meters To Centimeters")
            option_2 = int(input("Please enter the number of your choice: "))
            if option_2 == 0:
                break

            elif option_2 == 1:
                kilometers = float(input("Please enter a Kilometers to convert to Miles: "))
                print(f"{kilometers} kilometers = {km_to_miles(kilometers)} miles")

            elif option_2 == 2:
                miles = float(input("Please enter a Miles to covert to Kilometers: "))
                print(f"{miles} miles = {miles_to_km(miles)} kilometers")

            elif option_2 == 3:
                centimeters = float(input("Please enter a Centimeters to covert to Meters: "))
                print(f"{centimeters} cm = {cm_to_m(centimeters)} m")

            elif option_2 == 4:
                meters = float(input("Please enter a Meters to covert to Centimeters: "))
                print(f"{meters} m = {m_to_cm(meters)} cm")

            else:
                print("[Error] This number is error.")

            print()

            option_4 = int(input("Please enter 1 to continue in this section or 2 to exit this section: "))
            if option_4 == 1:
                continue
            elif option_4 == 2:
                print("Good buy, and see you next time for this section!")
                break
            else:
                print("Sorry, this number is error.")
                break

    elif option_1 == 2:
        while True:
            print("0: Exit this section.")
            print("1. Celsius To Fahrenheit\n2. Fahrenheit To celsius")
            option_2 = int(input("Please enter the number of your choice: "))

            if option_1 == 0:
                print("Goodbye! See you next time.")
                break

            elif option_2 == 1:
                celsius = float(input("Please enter a degree Celsius to convert to Fahrenheit: "))
                print(f"{celsius}\u00B0C = {celsius_to_fahrenheit(celsius)}\u00B0F")

            elif option_2 == 2:
                fahrenheit = float(input("Please enter a degree Fahrenheit to convert to Celsius: "))
                print(f"{fahrenheit}\u00B0F = {fahrenheit_to_celsius(fahrenheit)}\u00B0C")

            else:
                print("[Error] This number is error!")

            print()

            option_4 = int(input("Please enter 1 to continue in this section or 2 to exit this section: "))
            if option_4 == 1:
                continue
            elif option_4 == 2:
                print("Good buy, and see you next time for this section!")
                break
            else:
                print("Sorry, this number is error.")
                break

    elif option_1 == 3:
        while True:
            print("0: Exit this section.")
            print("1. Kilogram To Pound\n2. Pound To Kilogram")
            print("3. Kilogram To gram\n4. Gram to Kilogram ")
            option_2 = int(input("Please enter the number of your choice: "))

            if option_1 == 0:
                print("Goodbye! See you next time.")
                break

            elif option_2 == 1:
                kilogram = float(input("Please enter a Kilograms to convert to Pounds: "))
                print(f"{kilogram} kilograms = {kilogram_to_pound(kilogram)} pounds")

            elif option_2 == 2:
                pound = float(input("Please enter a Pounds to convert to Kilograms: "))
                print(f"{pound} pounds = {pound_to_kilogram(pound)} kilograms")

            elif option_2 == 3:
                kilogram = float(input("Please enter a kilograms to covert to grams: "))
                print(f"{kilogram} kg = {kilogram_to_gram(kilogram)} g")

            elif option_2 == 4:
                gram = float(input("Please enter a grams to covert to kilograms: "))
                print(f"{gram} g = {gram_to_kilogram(gram)} kg")

            else:
                print("[Error] This number is error!")

            print()

            option_4 = int(input("Please enter 1 to continue in this section or 2 to exit this section: "))
            if option_4 == 1:
                continue
            elif option_4 == 2:
                print("Good buy, and see you next time for this section!")
                break
            else:
                print("Sorry, this number is error.")
                break

    elif option_1 == 4:
        while True:
            print("0: Exit this section.")
            print("1. Square meter To square foot\n2. Square foot To square meter")
            option_2 = int(input("Please enter the number of your choice: "))

            if option_1 == 0:
                print("Goodbye! See you next time.")
                break

            elif option_2 == 1:
                square_meter = float(input("Please enter a Square meter to convert to Square foot: "))
                print(f"{square_meter} square meters = {meter_to_foot(square_meter)} square foots")

            elif option_2 == 2:
                square_foot = float(input("Please enter a Square foot to convert to Square meter: "))
                print(f"{square_foot} square foots = {foot_to_meter(square_foot)} square meters")

            else:
                print("[Error] This number is error!")

            print()

            option_4 = int(input("Please enter 1 to continue in this section or 2 to exit this section: "))
            if option_4 == 1:
                continue
            elif option_4 == 2:
                print("Good buy, and see you next time for this section!")
                break
            else:
                print("Sorry, this number is error.")
                break

    elif option_1 == 5:
        while True:
            print("0: Exit this section.")
            print("1. Canadian Dollars To Chinese Yuan\n2. Chinese Yuan To Canadian Dollars")
            print("3. Canadian dollars To GBP\n4. GBP To Canadian dollars")
            option_2 = int(input("Please enter the number of your choice: "))
            if option_1 == 0:
                print("Goodbye! See you next time.")
                break

            elif option_2 == 1:
                dollars_ca = float(input("Please enter a Canadian Dollars to convert to Chinese Yuan: "))
                print(f"{dollars_ca} Canadian Dollars = {dollars_ca_to_yuan(dollars_ca)} Chinese Yuan")

            elif option_2 == 2:
                yuan = float(input("Please enter a Chinese Yuan to convert to Canadian Dollars: "))
                print(f"{yuan} Chinese Yuan = {yuan_to_dollars_ca(yuan)} Canadian Dollars")

            elif option_2 == 3:
                dollars_ca = float(input("Please enter a Canadian Dollars to covert to GBP: "))
                print(f"{dollars_ca} Canadian Dollars = {dollars_ca_to_gbp(dollars_ca)} GBP")

            elif option_2 == 4:
                gbp = float(input("Please enter a GBP to covert to Canadian Dollars: "))
                print(f"{gbp} GBP = {gbp_to_dollars_ca(gbp)} Canadian Dollars")

            else:
                print("[Error] This number is error!")

            print()

            option_4 = int(input("Please enter 1 to continue in this section or 2 to exit this section: "))
            if option_4 == 1:
                continue
            elif option_4 == 2:
                print("Good buy, and see you next time for this section!")
                break
            else:
                print("Sorry, this number is error.")
                break

    elif option_1 == 6:
        while True:
            print("0: Exit this section.")
            print("1. Milliliter To Liter \n2. Liter To Milliliter")
            option_2 = int(input("Please enter the number of your choice: "))
            if option_1 == 0:
                print("Goodbye! See you next time.")
                break

            elif option_2 == 1:
                ml = float(input("Please enter a Milliliter to convert to Liter: "))
                print(f"{ml} Milliliter = {ml_to_l(ml)} Liter")

            elif option_2 == 2:
                l = float(input("Please enter a Liter to convert to Milliliter: "))
                print(f"{l} Liter = {l_to_ml(l)} Milliliter")
            else:
                print("[Error] This number is error!")

            print()

            option_4 = int(input("Please enter 1 to continue in this section or 2 to exit this section: "))
            if option_4 == 1:
                continue
            elif option_4 == 2:
                print("Good buy, and see you next time for this section!")
                break
            else:
                print("Sorry, this number is error.")
                break

    else:
        print("[Error] This number is error.")

    option_3 = int(input("Please enter 1 to continue in this program or 2 to exit program: "))

    if option_3 == 1:
        continue

    elif option_3 == 2:
        print("Good buy, and see you next time!")
        break

    else:
        print("Sorry, this number is error.")
        continue


