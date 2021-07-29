"""
project 1 login form v3
"""
username = "Montreal123"
password = "Montreal123"
print("To teacher, your username is {} and your password is {}"
      .format(username, password))

print("====== Login Form =======")
print("Welcome to login Bus Card Montreal!")
username1 = input("Please input your username: ")
password1 = input("Please input your password: ")
if username1 == username and password1 == password:
    print("Welcome to your sign in your page of Bus Card, your username is {} and your password is {}."
          .format(username, password))
    print("Good bye!")

elif username1 == username and password1 != password:
    print("Sorry your password is invalid. Please try again!")
    for i in range(1, 6):
        print("Important : your just have {} times to enter your password for security reasons.".format(6-i))
        password1 = input("Please input your password again: ")
        if password1 == password:
            print("Good bye!")
            print("Welcome to your sign in your page of Bus Card, your username is {} and your password is {}."
                  .format(username, password))
            break
    if 6-i == 1:
        print("Sorry,your account has been locked for security reasons.")

else:
    print("Sorry, your username is not correct, Please try again and restart.")
