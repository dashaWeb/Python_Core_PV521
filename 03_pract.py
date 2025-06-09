# Завдання 5
# Користувач із клавіатури вводить тризначне число. Наприклад, 891. Потрібно показати на різних рядках значення першого, другого і третього розряду. Також потрібно показати на окремому рядку суму цих трьох чисел. У нашому випадку це виглядатиме так:
# number //= 10 # number = number // 10
# number = int(input("Enter number -> ")) # 891

# a = number % 10 # number % 10 (891 % 10 = 1)
# number //= 10 # 891 / 10 => 89.1 => 89
# b = number % 10 # number % 10 (89 % 10 = 9)
# c = number // 10  # 89 // 10 = 8
# print(c)
# print(b)
# print(a)
# print(f"Sum : {a + b + c}")

# Завдання 6
# Користувач вводить суму вкладу та відсоткову ставку. Напишіть програму, яка:

# Обчислює, скільки користувач отримає через 5 років, якщо щороку сума вкладу збільшується на вказаний відсоток.
# Виводить суму вкладу за кожен рік окремо.

# money = int(input("Enter money :: ")) # 1000
# percent = int(input("Enter percent :: ")) # 10%

# # year_1 = money + money / 100 * percent
# # year_2 = year_1 + year_1 / 100 * percent
# money += money / 100 * percent
# print(f"Year 1 --> {money}")
# money += money / 100 * percent
# print(f"Year 2 --> {money}")
# money += money / 100 * percent
# print(f"Year 3 --> {money}")
# money += money / 100 * percent
# print(f"Year 4 --> {money}")
# money += money / 100 * percent
# print(f"Year 5 --> {money}")

# print(chr(9556),end="")
# print(chr(9552)*50, " "*50, chr(9552)*50)
# first = int(input("enter first ::"))
# second = int(input("enter second ::"))
# a = 99 - first + second 
# print(a)

# Завдання 9

# Користувач вводить з клавіатури розмір одного файлу в гігабайтах і швидкість
# інтернет-з’єднання в бітах на секунду. Порахувати, за скільки годин, хвилин і секунд
# завантажується файл.

size = int(input("Enter size file :: "))
speed = int(input("Enter speed :: "))
size = size * 8 * 1024 * 1024 * 1024

seconds = size // speed
h = seconds // 3600
seconds %= 3600
m = seconds // 60
seconds %= 60
print(f"{h}:{m}:{seconds}")