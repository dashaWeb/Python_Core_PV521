# Завдання 5
# Напишіть програму, яка аналізує файл log.txt, визначає 10 найпоширеніших слів, що зустрічаються найчастіше, і записує їх разом з їхньою частотою в word_stats.txt.

import re
list_words = []
list_count = []
try:
    with open("16_files/log.txt") as file:
        text = file.read()
    words = re.findall('\w+',text)
    for i in range(len(words)):
        flag = True
        for j in range(i):
            if words[i] == words[j]:
                flag = False
                break
        if flag:
            list_words.append(words[i])
            list_count.append(words.count(words[i]))
    for i in range(len(list_words)):
        print(list_words[i], " : ", list_count[i])  
    with open('16_files/word_stats.txt','w') as file:
        for i in range(10):
            max_ = max(list_count)
            index_ = list_count.index(max_)
            file.write(f"{list_words[index_]} :: {list_count[index_]} \n")
            list_words.pop(index_)
            list_count.pop(index_)  
except Exception as msg:
    print(msg)