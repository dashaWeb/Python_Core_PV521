# exaple 1
# number = input("Enter number :: ")
# number = int(number)

# print(f"Number :: {number}")
# print("Finally code")

# try:
#     number = input("Enter number :: ")
#     number = int(number)

#     print(f"Number :: {number}")
#     print("Finally code")
# except:
#     print("Run block except")

# example 2

# while True:
#     try:
#         test = True
#         number_1 = int(input("Enter number :: "))
#         number_2 = int(input("Enter number :: "))
#         print(f"Result :: {number_1} / {number_2} = {number_1 / number_2} {test}")
#         print("End code")
        
#     except ValueError as msg:
#         print(f"Run block ValueError :: message :: {msg}")
#     except ZeroDivisionError as msg:
#         print(f"Run block ZeroDivisionError :: message :: {msg}")
#     except (TypeError, NameError) as msg:
#         print(f"Run block NameError or TypeError :: message :: {msg}")
#     except Exception as msg:
#         print(f"Run block Exception :: message :: {msg}")
#     else:
#         print("Finally block try -=-> Run block else")
#         break
#     finally:
#         print("Disconnection")

# print("End program")


# def printNumber(number):
#     if number < 0:
#         raise ValueError(f"{number} < 0")
#     if number > 10_000:
#         raise Exception(f"{number} > 10 000")
#     print(f"Print number :: {number}")



# while True:
#     try:
#         number = int(input("Enter value :: "))
#         printNumber(number)
#         raise Exception("Test ggg")
#     except ValueError as msg:
#         print(f"Run block ValueError :: message :: {msg}")
#     except Exception as msg:
#         print(f"Run block Exception :: message :: {msg}")
#         break

# print("End program")

# Попросіть користувача ввести послідовність чисел через пробіл.

# У блоці try перетворіть рядок на список чисел. Для кожного елемента використовуйте вкладений блок try для перетворення на число, перехоплюючи ValueError для некоректних значень з виведенням попередження і пропуском таких елементів.
# Після успішного перетворення обчисліть суму і, якщо потрібно, середнє значення. Перехопіть ZeroDivisionError, якщо список виявиться порожнім.
# У блоці finally виведіть повідомлення про завершення обробки даних.

numbers = input("Enter numbers :: ")

try:
    numbers = numbers.split()
    print(numbers)
    i = 0
    while True:
        if i == len(numbers):
            break
        print(i)
        try:
            number = int(numbers[i])
            numbers[i] = number
            i+=1
        except ValueError:
            numbers.remove(numbers[i])
            
except ValueError:
    print(numbers)
print(numbers)
