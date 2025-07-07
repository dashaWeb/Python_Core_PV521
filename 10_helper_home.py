# Завдання 3
# Користувач з клавіатури вводить список чисел. Необхідно знайти у списку найдовшу послідовність елементів, що зростають, і вивести її довжину та самі елементи.

# Приклад:

# Вхідні дані:

# Список чисел: 1, 2, 1, 2, 3, 4, 1.
# Очікуваний результат:

# Довжина послідовності: 4.
# Послідовність: [1, 2, 3, 4].

import random
arr = [random.randint(1,10) for i in range(10)]
# arr = [1, 2, 1, 2, 3, 4, 5]
print(f'Print:: {arr}')

counter = 1
max_counter = 0
max_index = 0
index = 0
for i in range(len(arr)-1):
    if arr[i] < arr[i + 1]:
        counter += 1
        if counter > max_counter:
            max_counter = counter
            max_index = index
    else:
        index = i + 1
        counter = 1

print(max_counter, max_index)
print(arr[max_index:max_index + max_counter])