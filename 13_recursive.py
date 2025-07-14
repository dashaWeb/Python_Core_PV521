

# 5! = 5 * 4!
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1!
# 1! = 1
# 0! = 1

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)

print("Factorial :: ",fact(5))


# [1, 10]
# 1 2 3 4 5 6 7 8 9 10

def printRange(a,b):
    print(a, end="\t")
    if a == b:
        print()
        return
    printRange(a+1, b)

printRange(1,10)