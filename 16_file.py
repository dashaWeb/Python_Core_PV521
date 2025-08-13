# open
# read
# write
# close

# r"C:\Users\konopelko\Desktop\main.css"
# "../main.css"
# \n
# file = open("../main.css")
# allText = file.read()
# print(allText)
# file.close()

url = "16_files/text.txt"
# file = None
# try:
#     file = open(url)
#     print(file.read())
# except Exception as msg:
#     print(msg)
# finally:
#     file.close()
#     pass

# with open(url) as file:
#     print(file.readline())
#     file.seek(0)
#     print(file.readlines())
#     file.seek(0)
#     print(file.read(5))
#     print(file.readline(10))
#     file.seek(0)
#     print("="*50)
#     i = 1
#     for line in file:
#         print(i, line)
#         i+=1

# with open("16_files/data.txt", 'w') as file:
#     for i in range(3):
#         file.write(f"Test Line {i+1}\n")


# numbers = [1,2,53,4,7,844,5,4]
# numbers = map(lambda x: str(x) + "\n", numbers)
# with open("16_files/numbers.txt", 'w') as file:
#     file.writelines(numbers)

# words = map(lambda x : x + "\n","Сніг Дощ Хмара Сонце".split())
# with open("16_files/words.txt","w+",encoding="utf-8") as file:
#     file.writelines(words)


# with open("16_files/words.txt","r+",encoding="utf-8") as file:
#     print(file.read())


#task 6

def next_letter(n):
    lett = chr(ord(n) + 1)
    if n.isupper() and lett > 'Z':
        return 'A'
    if n.islower() and lett > 'z':
        return 'a'
    return lett

with open('16_files/data.txt') as file:
    text = file.read()

print(text)
for i in text:
    if not i.isalpha():
        continue
    text = text.replace(i, next_letter(i),1)
print(text)

with open('16_files/data.txt','w') as file:
    file.write(text)