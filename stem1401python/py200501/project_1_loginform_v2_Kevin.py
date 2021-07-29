"""
Project 1. Login Form
project_1_loginform_v1_Kevin.py
"""

# A title or name of the application is required to show at first.
print("Welcome to create your new account for your Bus card Montreal account! ")

# Users can input their username
username = input("Please enter your username of your Bus card Montreal: ")

# Users can input their password
password = input("Please enter your password of your Bus card Montreal: ")

# The System then echo the username and password and say hello!
print("Hello, so your username for your Bas card Montreal account is {}, and your password is {}!".format(username, password))

# The program ends with "Goodbye!"
print("Thank you for creation your account of Bus card Montreal, Goodbye!")

print("After 3 seconds, you will going to login your account")

print("======Login Form=======")
print("Welcome to login Bus Card Montreal!")
username1 = input("Please input your username: ")
if username1 == username:
    password1 = input("Please input your password: ")
    if password1 == password:
        print("Welcome to your account of Bus Card Montreal!")
        print("Sorry, your card hasn't good activate, for activate your card, "
              "please call to costumer center, thank you")

else:
    input1 = input("Sorry this is a unavailable username! If you want to try again, please click Yes for continue:")

# a1 = 1
# if input1 == a1:
#     username1 = input("Please input your username again: ")
# else:
#     print("Goodbye, see you soon!")






