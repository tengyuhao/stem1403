"""
project_converter_v1_demo
Menu level 1 - Choose a converter type
Menu level 2 - Choose a converting method

需检查：
- 语法, 结构
- 词汇
- 公式是否正确

"""


# Menu level 1 - Choose a converter type
print("Please choose a converter type:")
print("1. Length or distance")
print("2. Temperature")
print("3. Weight or mass")
print("4. Area")
n = float(input("Please enter the number of you choose:  "))


# Menu level 2 - Choose a converting method

# 1.1 and 1.2 (kilometers -> miles and miles -> kilometers)
if n == 1.0:
    print("1 kilometers To miles")
    print("1 miles To kilometers")
    n2 = float(input("Please chose 1 number enter 1 or 2: "))

    if n2 == 1.1:
        n3 = float(input("Please enter one number to calculate kilometers to miles: "))

        # 1km = 1000m
        def km_to_m(n3):
            n3 = n3 * 1000
            return n3


        print(f"{n3}km = {km_to_m(n3)}m")

    elif n2 == 1.2:
        n3 = float(input("Please enter one number to calculate miles to kilometers: "))

        # 1000m = 1km
        def m_to_km(n3):
            n3 = n3 / 1000
            return n3

        print(f"{n3}m = {m_to_km(n3)}km")

    else:
        print("This number is error!")


# 2.1 and 2.2 (Celsius -> Fahrenheit and Fahrenheit -> celsius)
elif n == 2.0:
    print("2.1 Celsius To Fahrenheit")
    print("2.2 Fahrenheit to celsius")
    n2 = float(input("Please chose 1 number enter 2.1 or 2.2: "))
    if n2 == 2.1:
        n = float(input("Please enter one number to calculate Celsius To Fahrenheit: "))

        # n * 1.8 + 32
        def c_to_f(n):
            n = n * 1.8 + 32
            return n


        print(f"{n}\u00B0C = {c_to_f(n)}\u00B0F")

    elif n2 == 2.2:
        n = float(input("Please enter one number to calculate Fahrenheit to celsius: "))

        # n / 1.9 - 32
        def f_to_c(n):
            n = n / 1.8 - 32
            return n


        print(f"{n}\u00B0F = {f_to_c(n)}\u00B0C")

    else:
        print("This number is error!")


# 3.1 and 3.2 (kilogram -> pound and Pound -> kilogram)
elif n == 3.0:
    print("3.1 kilogram to kilogram")
    print("3.2 pound to kilogram")
    n2 = float(input("Please chose 1 number enter 2.1 or 2.2: "))
    if n2 == 2.1:
        n = float(input("Please enter one number calculate kilogram to kilogram: "))

        # n * 1.8 + 32
        def kilogram_to_pound(n):
            n = n * 2.20462262
            return n


        print(f"{n}kilogram = {kilogram_to_pound(n)}pound")

    elif n2 == 2.2:
        n = float(input("Please enter one number to calculate pound to kilogram: "))


        def pound_to_kilogram(n):
            n = n / 2.20462262
            return n


        print(f"{n}pound = {pound_to_kilogram(n)}kilogram")

    else:
        print("This number is error!")

# 4.1 and 4.2 (Square meter -> square foot and square foot -> Square meter)
elif n == 4.0:
    print("4.1 Square meter to square foot")
    print("4.2 Square foot to square meter")
#   0.09290304
    n2 = float(input("Please chose 1 number enter 2.1 or 2.2: "))
    if n2 == 2.1:
        n = float(input("Please enter one number to calculate Square meter to square foot: "))

        #
        def meters_to_foot(n):
            n = n / 0.09290304
            return n


        print(f"{n}square meter = {meters_to_foot(n)}square foot")

    elif n2 == 2.2:
        n = float(input("Please enter one number to calculate Square foot to square meter: "))


        def foot_to_meters(n):
            n = n * 0.09290304
            return n


        print(f"{n}square foot = {foot_to_meters(n)}square meter")

    else:
        print("This number is error!")


# else: error
else:
    print("This number is error!")



