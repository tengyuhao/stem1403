"""

"""

import random

print("Official Customer Service. Welcome to ....")
print("Welcome! Start to input your information to register.")


try:
    first_name = input("Please input your first name : ")
    last_name = input("Please input your last name : ")
    e_mail = input("Please input your e-mail : ")
    print("What do you want to say to our customer service.")
    info = input("So, please write here : ")

except ValueError as ve:
    print(ve)
except KeyboardInterrupt as ki:
    print(ki)
except Exception as e:
    print(e)

seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$"
sa = []
for i in range(8):
    sa.append(random.choice(seed))
id = ''.join(sa)


print("Please note this ID, if you want to call to our customer service, this code is very important")
print(f"This is your ID {id}")

try:
    file = open("informations.txt", 'a')
    file.writelines(["First name : ", first_name, "\nLast name : ", last_name, "\nE-mail: ", e_mail, "\nID : ", id, "\n\n"])
    file.close()
    print("Your information is registed, please wait our customer service to contact with you.")
except FileExistsError as fee:
    print(fee)
except Exception as e:
    print(e)
    print("Error, error code : FILE-1227. Please call this telephone.")


