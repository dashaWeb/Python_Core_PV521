# word = "hello"

# for letter in word: # [h,e,l,l,o]
#     print(letter + " - ", end='')
# print()

# for i in range(10): # [0,1,2,3,4,5,6,7,8,9]
#     print(i + 1, end="\t")

# start = 1
# end = 10
# print()
# for el in range(start, end+1): #[1,2,3,4,5,6,7,8,9 ]
#     print(el,end="\t")
# print()


# for i in range(2,21, 2):
#     print(i, end="\t")

# number = int(input("Enter number :: "))#8
# counter = 0
# # range() => 1,2,3,4,5,6,7,8
# # number{8} % 1 --> True --> counter{0} +=1 (counter{1})
# # number{8} % 2 --> True --> counter{1} +=1 (counter{2})
# # number{8} % 3 --> False --> 
# # number{8} % 4 --> True --> counter{2} +=1 (counter{3})
# # number{8} % 5 --> False --> 
# # number{8} % 6 --> False --> 
# # number{8} % 7 --> False --> 
# # number{8} % 8 --> False --> counter{3} +=1 (counter{4})

# for i in range(1, number+1):
#     if number % i == 0:
#         counter+=1
# else:
#     print(counter)

# if counter > 2:
#     print("Complex number")
# else:
#     print("Prime number")

# number = int(input("Enter number :: "))#8

# flag = True 
# for i in range(2, number//2):
#     if number % i == 0:
#         flag = False
#         break

# if flag:
#     print("Prime number")
# else:
#     print("Complex number")

import random

# for i in range(10):
#     # rnd = random.random() # 0 - 1
#     # rnd = int(random.random() * 10 + 1)
#     # rnd = random.randint(1,10)
#     rnd = random.choice("spr")
#     print(rnd, end="\t")
#     # input()

user_win = 0
bot_win = 0
draw = 0

while True:
    bot_score = 0
    user_score = 0
    for i in range(5):
        print('-'*15 + f" Round #{i+1} " + '-'*15)
        while True:
            user = input('''
                [r] - rock
                [s] - scissors
                [p] - paper
                [l] - lizard
                [v] - spock
                    enter choice :: ''')
            if user == 'r' or user == 'p' or user == 's' or user == 'sp' or user == 'l':
                break
            else:
                print("\033[31m Error!!! Enter true choice \033[0m")
        bot = random.choice('rsplv')
        print(f"\t\t Bot \t User")
        print(f"\t\t [{bot}] \t [{user}]")

        if user == 'r' and bot == 's' or user == 'r' and bot == 'l'  or user == 's' and bot == 'p' or user == 's' and bot == 'l' or user == 'p' and bot == 'r' or user == 'p' and bot == 'v' or user == 'l' and bot == 'p' or user == 'l' and bot == 'v' or user == 'v' and bot == 's' or user == 'v' and bot == 'r':
            user_score +=1
        elif user != bot:
            bot_score+=1

    if user_score > bot_score:
        print('-'*15 + f" Congratulation!!! " + '-'*15)
        user_win +=1
    elif bot_score > user_score:
        print('-'*15 + f" Sorry! You Loser " + '-'*15)
        bot_win +=1
    else:
        print('-'*15 + f" Draw " + '-'*15)
        draw+=1

    exit = input("Play again [yes/no] --> ")
    if exit == "no":
        break

print(f'''
    Bot  win - [{bot_win}]
    User win - [{user_win}]
    Draw     - [{draw}]
''')




# 1 - Реалізувати можливість (розпочати гру знову)
# 2 - Розширити гру додавши нові варіант (ящірка, спок)
# 3 - Збільшити кількість раундів до 5-ти
# Коли користувач завершить гру (вийшов) - показати статистику по всій грі
#  User won - 2
#  Bot  won - 2
#  Draw - 2