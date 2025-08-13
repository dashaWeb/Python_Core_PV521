# test = [True, "Test", 145, 45.2]
# print(test)


colors = ["red","purple","yellow","orange","blue"]
print(f"Id : {id(colors)} \t Type :: {type(colors)} \t Value : {colors} \t Length : {len(colors)}")

print(colors[2])
colors[2] = "lime"
print(colors)

# colors[5] = "magenta" Error
print('yellow' in colors)
print('lime' in colors)

# [start:end:step]
print(colors[:2])
print(colors[0:len(colors):2])
print(colors[::2])
print(colors[2:])
print(colors[::-1])

# i = 0
# while i < len(colors):
#     print(colors[i].upper())
#     i+=1

for item in colors:
    print(item)

print()

# додає новий елемент в кінець  списка
print("colors.append")
print(f"Before :: {colors}")
colors.append("gold")
print(f"After  :: {colors}")


# додає новий елемент за вказаним індексом
print("colors.insert")
print(f"Before :: {colors}")
colors.insert(2,"green")
print(f"After  :: {colors}")

# додає списк до поточного списка
print("colors.extend")
print(f"Before :: {colors}")
colors.extend(["cyan","brown","pink"])
print(f"After  :: {colors}")

print()
# видаляє елемент за індексом
print("colors.extend")
print(f"Before :: {colors}")
colors.pop(2)
print(f"After  :: {colors}")

# видаляє елемент за вмістом
print("colors.extend")
print(f"Before :: {colors}")
if "while" in colors:
    colors.remove("white")
print(f"After  :: {colors}")

# colors.clear()
# print(colors)

# print(f"Index :: {colors.index("gold")}")
for i in range(4):
    colors.append("red")

print(f"List :: {colors}")
print(colors.count("red"))

# [a - z]
colors.sort()
print(f"List :: {colors}")
# [z - a]
colors.sort(reverse=True)
print(f"List :: {colors}")
colors.reverse()
print(f"List :: {colors}")


numbers = [1,5,4,7,8,5,1,2,3,4]
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))
print(sorted(numbers, reverse=True))


print(numbers)
clone = numbers.copy()
print(f"Id :: {id(numbers)}")
print(f"Id :: {id(clone)}")

clone[1] = 333

print(numbers)
print(clone)

# marks = []
# for i in range(5):
#     n = int(input("Enter number :: "))
#     marks.append(n)
# 10 11 12 10
marks = [int(i) for i in input("Enter number :: ").split(" ")]
marks = [str(i) for i in marks]
print(marks)
print(",".join(marks))