import random
prices = [random.randint(100, 500) for i in range(10)]


def lowPrice(collection):
    clone = collection.copy()
    for i in range(len(clone)):
        clone[i] = low(clone[i])

    return clone


def low(item):
    return item - item * 0.05


def printPrice(collection, prompt=""):
    print(prompt, end="")
    for item in collection:
        print(item, end="\t")
    print()


printPrice(prices, "Before :: ")
printPrice(lowPrice(prices), "After  :: ")
printPrice(prices, "Before :: ")

printPrice(list(map(lambda item: item + item * 0.10, prices)), "After  :: ")
printPrice(list(map(lambda item: item - item * 0.10, prices)), "After  :: ")
printPrice(list(map(lambda item: item * 2, prices)), "After  :: ")
printPrice(list(map(lambda item: item / 2, prices)), "After  :: ")
printPrice(list(map(lambda item: 100, prices)), "After  :: ")


# marks = input("Enter marks :: ").split()
# marks = list(map(lambda item: int(item), marks))
# print(sum(marks) / len(marks))

# showMessage = lambda : print("Hello")
# showMessage()

# sum_ = lambda a,b : a + b
# print(sum_(7,5))

print()
start = int(input("Enter start :: "))
end = int(input("Enter end :: "))

printPrice(prices)
printPrice(filter(lambda x: x >= start and x <= end,prices))