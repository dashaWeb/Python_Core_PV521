# print(13, type(13)) # number (int)
# print(13.5, type(13.5)) # number (float)
# print("Hello", type("Hello")) # string (str)
# print(True, type(True)) # boolean (bool)


# first_name = "Alex" # string (str)
# age = 18 #number(int)
# PI = 3.14
# flag = True
# print(first_name, type(first_name))
# print(age, type(age))
# print(PI, type(PI))
# print(flag, type(flag))
# PI = 4.12
# print(PI, type(PI))

# name = "Ivan"
# number = 5
# result = name / 5

'''
    /
    *
    +
    -
    %
    //
    **

    ()
    //,**,%
    /,*
    +,-
'''

# one = 7
# two = 5
#  7 + 5 = 12
# one, two = 9, 5
# result_sum = one + two
# print(one, "+", two, "=", result_sum)
# print("{} + {} = {}".format(one, two, result_sum))
# print(f"{one} + {two} = {one + two}")
# print(f"{one} - {two} = {one - two}")
# print(f"{one} * {two} = {one * two}")
# print(f"{one} / {two} = {one / two}")
# print(f"{one} // {two} = {one // two}")  # 1
# print(f"{one} % {two} = {one % two}")  # 1
# one, two = 2, 4
# print(f"{one} ** {two} = {one ** two}")  # 1

# # 1 * 10^30
# big_number = 10e-5#1000000000000000000000000000000
# print(big_number)

# True(1) False(0)
# number = 13
# flag = True
# result = number + flag # 13 + 1
# print(f"Result :: {result} {type(result)}")
# result = number + 3.14
# print(f"Result :: {result} {type(result)}")
# result = number + "3"

# int()
# float()
# str()
# bool()

# one = int(input("Enter number :: "))
# two = input("Enter number :: ")
# two = int(two)
# print(f"{one} + {two} = {one + two}")
# print(int(float("45.5")))
# print(bool(0))

# Завдання 2
# Користувач вводить із клавіатури два числа. Перше число — це значення, друге число відсоток, який необхідно порахувати. Наприклад, ми ввели з клавіатури 50 і 10. Потрібно вивести на екран 10 відсотків від 50. Результат: 5.

number = int(input("Enter number :: "))
percent = int(input("Enter percent :: "))

# 1500 
# 15%
# way = 1500 * 0.15
# way2 = 1500 / 100 * 15 
print(f"{percent}% = {number * (percent / 100)}")
print(f"{percent}% = {number / 100 * percent}")