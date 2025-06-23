# Завдання 5
# Користувач вводить два числа, що представляють діапазон. Програма повинна пройти по діапазону і вивести добуток усіх чисел, які діляться на 4, але не діляться на 6. Якщо таких чисел немає, вивести відповідне повідомлення. Діапазон має автоматично нормалізуватися, якщо початок більший за кінець.

#  1 2 3 4 5 6 7 8 9 10

# start = int(input("Enter start range :: "))
# end = int(input("Enter end range :: "))

# if start > end:
#     start,end = end, start
# mult = 1
# # mult = mult{1} * 4 = mult{4}
# # mult = mult{4} * 8 = mult{32}
# # mult = mult{32} * 16
# # mult = mult{--} * 20
# numb = start
# while numb <= end:
#     if numb % 4 == 0 and numb % 6 !=0:
#         mult*=numb
#     numb += 1
# if mult > 1 :
#     print(f"Result :: {mult}")
# else:
#     print("number not found")

# Завдання 6
# Користувач вводить два числа: число A і ступінь N, у який потрібно піднести число. Програма повинна обчислити A у степені N за допомогою циклу (без використання вбудованих функцій піднесення до степеня).

# number = int(input("Enter number :: "))
# step = int(input("Enter step :: "))
# mult = number
# step-=1
# #  2 ^ 4 ==> 2 * 2 * 2 * 2
# # mult = mult{2} * 2
# # mult = mult{4} * 2
# # mult = mult{8} * 2
# while step > 0:
#     step-=1
#     mult *= number
# print(f"Result : {mult}")

# Завдання 4
# Користувач вводить два числа і крок (інтервал), з яким потрібно проходити по діапазону. Програма має показати числа від початку діапазону до кінця, збільшуючи кожне число на вказаний крок. Також програма повинна надавати вибір порядку виведення: у прямому або зворотному порядку.
# start = int(input("Enter start range :: ")) #1
# end = int(input("Enter end range :: "))#15
# step = int(input("Enter step :: "))
# # 1, 3,5,7,9,11,13,15

# if start > end:
#     start,end = end, start

# choice = int(input('''
#     [1] - Abc
#     [2] - Desc
#         Enter choice :: '''))
# if choice == 1:
#     while start <= end:
#         print(start, end='\t')
#         start+=step
# elif choice == 2:
#     while end >= start:
#         print(end, end='\t')
#         end-=step
# else:
#     print("Error")
# print()