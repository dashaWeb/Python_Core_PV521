import re
def printMessage(name = "", last_name = ""):
    print(f"Hello \n First name : {name} \n Last name : {last_name}")


printMessage(last_name="Bondar")
printMessage("Sasha")
printMessage("Pasha")


def summ(a,b):
    return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    if b == 0:
        print("Error! Division by zero!")
    else:
        return a / b


def calculate(a,b, op):
    match op:
        case '+' :
            return summ(a,b)
        case '-':
            return sub(a,b)
        case '*':
            return mult(a,b)
        case '/':
            return div(a,b)
    print("Error operation")

def findOperation(input):
    match = re.search('[+-\/\*]',input)
    return match[0] if match else None


def printRes(input):
    if len(input) < 3:
        print("Error!!!")
        return
    elif len(input.split()) == 3:
       input = input.split()
       op = input[1]
       numb_2 = int(input[2])
    else:
        match = findOperation(input)
        if match:
            input = input.split(match)
            op = match
            numb_2 = int(input[1])
        else:
            return
    numb_1 = int(input[0])
    
    print(f"{numb_1} {op} {numb_2} = {calculate(numb_1,numb_2,op)}")


numb_1 = 5
numb_2 = 7

print(f"{numb_1} + {numb_2} = {summ(numb_1,numb_2)}")
print(f"{numb_1} - {numb_2} = {sub(numb_1,numb_2)}")
print(f"{numb_1} * {numb_2} = {mult(numb_1,numb_2)}")
print(f"{numb_1} / {numb_2} = {round(div(numb_1,numb_2),2)}")

# ex = input("Enter :: ")#.split() #2 + 2 ['2', '+', '2']

# printRes(ex)


def sum_all(*numbers):
    sum = 0
    for numb in numbers:
        sum += numb
    return sum

def printMatrix(mat, prompt = ""):
    print(prompt + " :: ") if len(prompt) > 0 else ""
    for row in mat:
        for item in row:
            print(item, end = "\t")
        print()

print(sum_all(1,2,3,4,5,6,7,8,9,))

import random
matrix = [[random.randint(1,20) for i in range(4)] for j in range(4)]
printMatrix(matrix, "Print matrix")