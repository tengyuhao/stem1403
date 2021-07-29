"""
Project 2 V2
"""

print()

# name and address
company_name = "CARTE ANNUELLE Parcs nationaux du Québec - Édition Bonjour Québec"
print("{:}{:>17}".format(company_name, "INVOICE"))

print()

address1 = "1912 Harvest Lane \nNew York, NY 12210"
print("{:}".format(address1))

print("\n\n\n")


# Bill TO, Ship TO, Invoice #, Invoice Date, P.O.# and Due Date
info = [
        ["Bill To", "Ship To", "Invoice #", "US-001"],
        ["John Smith", "John Smith", "Invoice Date", "11/02/2019"],
        ["2 Court Square", "3787 Pineview Drive", "P.O.#", "2312/2019"],
        ["New York, NY 12210", "Cambridge, MA 12210", "Due Date", "26/02/2019"]
]

print("{:<25}{:<22}{:>20}{:>15}".format(info[0][0], info[0][1], info[0][2], info[0][3]))
print("{:<25}{:<22}{:>20}{:>15}".format(info[1][0], info[1][1], info[1][2], info[1][3]))
print("{:<25}{:<22}{:>20}{:>15}".format(info[2][0], info[2][1], info[2][2], info[2][3]))
print("{:<25}{:<22}{:>20}{:>15}".format(info[3][0], info[3][1], info[3][2], info[3][3]))


# The table
print("\n")

# line
line1 = "------------------------------------"
line2 = "----------------------------------------------------------------------------------"
line3 = "__________________________________________________________________________________"

# first line
print(line3)
print("{:^7} {:^31} {:^20} {:^21}".format("QTY", "DESCRIPTION", "UNITE PRICE", "AMOUNT"))

item = [[1, "Front and real brake cables", 100.00],
        [2, "New set of pedal arms ", 15.00],
        [3, "Labor 3hrs", 5.00]
        ]

# item_1
amount_1 = item[0][0] * item[0][-1]
print("{:^7}{:<31}{:>20.2f}{:>24.2f}".format(item[0][0], item[0][1], item[0][2], amount_1))

# item_2
amount_2 = item[1][0] * item[1][2]
print("{:^7}{:<31}{:>20.2f}{:>24.2f}".format(item[1][0], item[1][1], item[1][2], amount_2))

# item_3
amount_3 = item[2][0] * item[2][2]
print("{:^7}{:<31}{:>20.2f}{:>24.2f}".format(item[2][0], item[2][1], item[2][2], amount_3))

print(line2)


# Tax and Subtotal
subtotal = amount_1 + amount_2 + amount_3
print("{:>61}{:>21.2f}".format("Subtotal", subtotal))

tax = subtotal * 0.0625
print("{:>61}{:>21.2f}".format("Sales Tax 6.25%", tax))


# Total
total = subtotal * 1.0625
print("{:>82}".format(line1))
print("{:>61}{:>21.2f}".format("TOTAL", total))


# terms & conditions

print("\n\n\n\n\n\n\n")

print("{}".format("Terms & Conditions"))
print("{}".format("Payment is due within 15 days"))

print()

print("{} {}".format("Please make checks payable to :", company_name))

# finish
print()



