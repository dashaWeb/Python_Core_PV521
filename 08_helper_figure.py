# *****
#  ***
#   *
#  ***
# *****

# print(" "*0 + "*"*5)
# print(" "*1 + "*"*3)
# print(" "*2 + "*"*1)
# print(" "*1 + "*"*3)
# print(" "*0 + "*"*5)

# line = 15
# q = 0
# j = line
# for i in range(line):
#     if i == line // 2 + 1:
#         q-=1
#         j+=2
#     if i < line // 2 + 1:
#         print(" "*q+ "*"*j)
#         q += 1
#         j-= 2
#     else:
#         q-=1
#         j+=2
#         print(" "*q+ "*"*j)
#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *
# print(' '*4 + '*' * 1)
# print(' '*3 + '*' * 2)
# print(' '*2 + '*' * 3)
# print(' '*1 + '*' * 4)
# print(' '*0 + '*' * 5)
# print(' '*1 + '*' * 4)
# print(' '*2 + '*' * 3)
# print(' '*3 + '*' * 2)
# print(' '*4 + '*' * 1)


# line = 21
# j = 0
# q = line // 2 + 1

# for i in range(line):
#     print(' ' * 15,end="")
#     if i < line // 2 + 1:
#         q-=1
#         j+=1
#         print(' '*q + '*' * j)
#     else:
#         q+=1
#         j-=1
#         print(' '*q + '*' * j)