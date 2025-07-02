
# matrix = [
#     [1,2,3, 20,21,25,23,85,96,85,35,45,48,78], #0
#     [4,5,6, 20,21,25,23,85,96,85,35], #1
#     [7,8,9, 20,21,25,23,85,96,85,35],  #2
#     [10,11,12, 20,21,25,23,85,96,85,35],  #3
#     [13,14,15, 20,21,25,23,85,96,85,35],  #4
#     [16,17,18, 20,21,25,23,85,96,85,35],  #5
# ]



# row 1
# print(matrix[0][0])
# print(matrix[0][1])
# print(matrix[0][2])

# print row 1
# for i in range(3): # 0 1 2 
#     print(matrix[0][i],end="\t")
# print()

# # print row 2
# for i in range(3): # 0 1 2 
#     print(matrix[1][i],end="\t")
# print()

# # print row 3
# for i in range(3): # 0 1 2 
#     print(matrix[2][i],end="\t")
# print()
# len(matrix)
# for j in range(len(matrix)): # 0 1 2 проходимо по рядках
#     for i in range(len(matrix[j])): # 0 1 2 проходимо по комірках (стовпцях)
#         print(matrix[j][i],end="\t")
#     print()


# for row in matrix:
#     for item in row:
#         print(item,end="\t")
#     print()

# import random
# # row = 3
# # col = 3
# row = col = 3
# matrix = []

# for i in range(row):
#     row_matrix = []
#     for j in range(col):
#         row_matrix.append(random.randint(1,20))
#     matrix.append(row_matrix)

# for row in matrix:
#     for item in row:
#         print(item,end="\t")
#     print()



import random
# row = 3
# col = 3
row = col = 3



# row_1 = [random.randint(1,20) for i in range(col)]
# row_2 = [random.randint(1,20) for i in range(col)]
# row_3 = [random.randint(1,20) for i in range(col)]
# matrix = [
#     row_1,
#     row_2,
#     row_3
# ]

# matrix = []
# for i in range(row):
#     matrix.append([random.randint(1,20) for i in range(col)])

# for row in matrix:
#     for item in row:
#         print(item,end="\t")
#     print()

# matrix = [[random.randint(1,10) for i in range(col)] for i in range(row)]

# for row in matrix:
#     for item in row:
#         print(item,end="\t")
#     print()

# sum_ = 0
# # for row in matrix:
# #     for item in row:
# #         sum_+= item
# for row in matrix:
#     sum_ += sum(row)

# min_ = matrix[0][0]
# max_ = matrix[0][0]
# for row in matrix:
#     for item in row:
#         if min_ > item:
#             min_ = item
#         if max_ < item:
#             max_ = item
        
# print(f"Sum :: {sum_}")
# print(f"Min :: {min_}")
# print(f"Max :: {max_}")

matrix = [[random.randint(1,10) for i in range(col)] for i in range(row)]
clone = matrix.copy()
for i in range(len(matrix)):
    clone[i] = matrix[i].copy()

for row in matrix:
    for item in row:
        print(item,end="\t")
    print()

print()

for row in clone:
    for item in row:
        print(item,end="\t")
    print()

print(f"Origin :: {id(matrix)}")
print(f"Clone  :: {id(clone)}")

clone[0][0] = 22

for row in matrix:
    for item in row:
        print(item,end="\t")
    print()

print()

for row in clone:
    for item in row:
        print(item,end="\t")
    print()