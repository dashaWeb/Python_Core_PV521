'''
    >
    <
    >=
    <=
    ==
    !=
'''


a = 5
b = 7

print(f"{a} > {b}  -->  {a > b}")  # False
print(f"{a} < {b}  -->  {a < b}")  # True
print(f"{a} >= {b}  -->  {a >= b}")  # False
print(f"{a} <= {b}  -->  {a <= b}")  # True
print(f"{a} == {b}  -->  {a == b}")  # False
print(f"{a} != {b}  -->  {a != b}")  # True

login = "mka"
print(f"login = 'Mka'  --> {login == 'Mka'}") # False
print(f"login = 'Mka'  --> {login == 'mka'}") # True


# and, or 
password = "mka5"

print(login == 'mka' and password == 'mka')
print(login == 'mka' and password == 'mka5')

# month = int(input("Enter month --> "))
# print(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12)



# year = int(input("Enter year --> "))

# days = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) + 365
# print(days)
# login = 'dev'
# if login == 'mka' and password == 'mka5':
#     print('Welcome')
# else:
#     print("Error")



# day = int(input("Enter number day :: "))
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# else:
#     print("Error")

# print("="*100)


# number = int(input("Enter number :: "))
# if number <= 20 and number >= 0:
#     print("number is in range")
# elif number > 20 or number < 0:
#     print("number is not in range")


# login = input("Enter login :: ")
# if login == "cancel":
#     print("login canceled")
# elif login == "admin":
#     password = input("Enter password :: ")
#     if password == "step":
#         print("Welcome")
#     elif password == "cancel":
#         print("login canceled")
#     else:
#         print("Error password")
# else:
#     print("I don't know you")



choice = int(input('''
    Select operation
        1 - sum
        2 - sub 
        3 - mult
        4 - div
        5 - avg
        Enter --> '''))

a = 5
b = 7

if choice == 1:
    print(f"{a} + {b} = {a+b}")
elif choice == 2:
    print(f"{a} - {b} = {a-b}")
else:
    print("Error. Enter true choice")
