

# while умова:
#     тіло цикла


# i = 1
# while i <= 10:
#     print(f"{i} Hello")
#     i+=1


# i = 0
# while i < 10:
#     i+=1
#     print(f"{i} Hello")
# else:
#     print("Finally")


# print("================")


# 10 9 8 7 6 5 4 3 2 1

# i = 10
# while i > 0:
#     print(i, end="\t")
#     i-=1
# print()

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

number = int(input("Enter number :: "))

i = 0
while i < number:
    i += 1
    print(i, end="\t")


start = 20
end = 1

if start > end:
    start, end = end, start

# print()
# while True:
#     answer = int(input("2 + 2 = "))
#     if answer == 4:
#         break
# else:
#     print("Finnaly")
# print("================")

# i = 0
# while i < 5:
#     color = input("Enter color :: ")
#     i+= 1
#     if color == "red":
#         continue
#     print(color)


# 12345
# 54321

# number{123} => number{123} % 10 --> 3
# number //= 10 => 123 // 10 --> 12
# number{12} => number{12} % 10 --> 2
# number //= 10 => 12 // 10 --> 1
# number{1} => number{1} % 10 --> 1
# number //= 10 => 1 // 10 --> 0

# res = 0
# res *= 10 -> {0}
# res += 3 -> {3}
# res *= 10 -> {30}
# res += 2 -> {32}
# res *= 10 -> {320}
# res += 1 -> {321}
# 3
# 2
# 1
# 321


# number = int(input("Enter number :: "))
# res = 0
# len = 0
# while number != 0:
#     digit = number % 10
#     len+=1
#     number //= 10
#     res *=10
#     res += digit
# else:
#     print(f"Result :: {res}")
#     print(f'Length :: {len}')


# number = int(input("Enter number :: "))
# len = 0
# while number != 0:
#     number //=10
#     len+=1
