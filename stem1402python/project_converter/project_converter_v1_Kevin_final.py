"""
project_converter_v1_final
Menu level 1 - Choose a converter type
Menu level 2 - Choose a converting method

"""


# Menu level 1 - Choose a converter type
print("Please choose a converter type:")
print("1. Length or Distance")
print("2. Temperature")
print("3. Weight or Mass")
print("4. Area")
option_1 = float(input("Please enter the number of your choice: "))


# Menu level 2 - Choose a converting method

# 1.1 and 1.2 (kilometers -> miles and miles -> kilometers)
if option_1 == 1.0:
    print("1. Kilometers To Miles")
    print("2. Miles To Kilometers")
    option_2 = float(input("Please enter the number of your choice: "))

    if option_2 == 1.0:
        kilometers = float(input("Please enter a Kilometers to convert to Miles: "))


        def km_to_miles(kilometers_1):
            miles_1 = kilometers_1 * 0.621371192
            return miles_1


        print(f"{kilometers} kilometers = {km_to_miles(kilometers)} miles")

    elif option_2 == 2.0:
        miles = float(input("Please enter a Miles to covert to Kilometers: "))


        def miles_to_km(miles_2):
            kilometers_2 = miles_2 / 0.621371192
            return kilometers_2

        print(f"{miles} miles = {miles_to_km(miles)} kilometers")

    else:
        print("This number is error!")


# 2.1 and 2.2 (Celsius -> Fahrenheit and Fahrenheit -> celsius)
elif option_1 == 2.0:
    print("1. Celsius To Fahrenheit")
    print("2. Fahrenheit To celsius")
    option_2 = float(input("Please enter the number of your choice: "))
    if option_2 == 1.0:
        celsius = float(input("Please enter a degree Celsius to convert to Fahrenheit: "))


        def celsius_to_fahrenheit(cel_degree):
            fahrenheit_1 = cel_degree * 1.8 + 32
            return fahrenheit_1


        print(f"{celsius}\u00B0C = {celsius_to_fahrenheit(celsius)}\u00B0F")

    elif option_2 == 2.0:
        fahrenheit = float(input("Please enter a degree Fahrenheit to convert to Celsius: "))


        def fahrenheit_to_celsius(fah_degree):
            celsius_2 = fah_degree - 32
            celsius_2 = celsius_2 / 1.8
            return celsius_2


        print(f"{fahrenheit}\u00B0F = {fahrenheit_to_celsius(fahrenheit)}\u00B0C")

    else:
        print("This number is error!")


# 3.1 and 3.2 (kilogram -> pound and Pound -> kilogram)
elif option_1 == 3.0:
    print("1. Kilogram To Pound")
    print("2. Pound To Kilogram")
    option_2 = float(input("Please enter the number of your choice: "))
    if option_2 == 1.0:
        kilogram = float(input("Please enter a Kilograms to convert to Pounds: "))


        def kilogram_to_pound(kilogram_1):
            pound_1 = kilogram_1 * 2.20462262
            return pound_1


        print(f"{kilogram} kilograms = {kilogram_to_pound(kilogram)} pounds")

    elif option_2 == 2.0:
        pound = float(input("Please enter a Pounds to convert to Kilograms: "))


        def pound_to_kilogram(pound_2):
            kilogram_2 = pound_2 / 2.20462262
            return kilogram_2


        print(f"{pound} pounds = {pound_to_kilogram(pound)} kilograms")

    else:
        print("This number is error!")

# 4.1 and 4.2 (Square meter -> square foot and square foot -> Square meter)
elif option_1 == 4.0:
    print("1. Square meter To square foot")
    print("2. Square foot To square meter")
    #   0.09290304
    option_2 = float(input("Please enter the number of your choice: "))
    if option_2 == 1.0:
        square_meter = float(input("Please enter a Square meter to convert to Square foot: "))


        def meter_to_foot(s_meter):
            s_foot = s_meter / 0.09290304
            return s_foot


        print(f"{square_meter} square meters = {meter_to_foot(square_meter)} square foots")

    elif option_2 == 2.0:
        square_foot = float(input("Please enter a Square foot to convert to Square meter: "))


        def foot_to_meter(s_foot_2):
            s_meter_2 = s_foot_2 * 0.09290304
            return s_meter_2


        print(f"{square_foot} square foots = {foot_to_meter(square_foot)} square meters")

    else:
        print("This number is error!")


# else: error
else:
    print("This number is error!")


