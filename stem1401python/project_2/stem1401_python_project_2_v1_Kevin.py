"""
Project 2 V1
/Users/kevinteng/PycharmProjects/stem1401python/py200513/project_2/stem1401_python_project_2_v1_Kevin.py
"""

# name and address
company_name = "East Repair Inc."
print("{:<}{:>74}".format("East Repair Inc.", "INVOICE"))

print()

print("{:<}".format("1912 Harvest Lane \nNew York, NY 12210"))

print("\n\n\n")

# Bill TO, Ship TO, Invoice #, Invoice Date, P.O.# and Due Date
print("{:<30}{:<25}{:>20}{:>15}".format("Bill To", "Ship To", "Invoice #", "US-001"))
print("{:<30}{:<25}{:>20}{:>15}".format("John Smith", "John Smith", "Invoice Date", "11/02/2019"))
print("{:<30}{:<25}{:>20}{:>15}".format("2 Court Square", "3787 Pineview Drive", "P.O.#", "2312/2019"))
print("{:<30}{:<25}{:>20}{:>15}".format("New York, NY 12210", "Cambridge, MA 12210", "Due Date", "26/02/2019"))

# The table
print("\n")

# first line
print("{:^7} {:^34} {:^20} {:^26}".format("QTY", "DESCRIPTION", "UNITE PRICE", "AMOUNT"))

# des_1
print("{:^7} {:<34} {:>20.2f} {:>26.2f}".format(1, "Front and real brake cables", 100.00, 100.00))

# description_2
print("{:^7} {:<34} {:>20.2f} {:>26.2f}".format(2, "New set of pedal arms ", 15.00, 30.00))

# description_3
print("{:^7} {:<34} {:>20.2f} {:>26.2f}".format(4, "Labor 3hrs", 5.00, 15.00))


# Tax and Subtotal
print("{:>63}{:>27.2f}".format("Subtotal", 145.00))

print("{:>63}{:>27.2f}".format("Sales Tax 6.25%", 9.06))

# Total
print("{:>63}{:>27.2f}".format("TOTAL", 154.06))


# terms and conditions
print("\n\n\n\n\n\n\n")

print("Terms & Conditions")
print("Payment is due within 15 days")

print()

print("Please make checks payable to: East Repair Inc.")




