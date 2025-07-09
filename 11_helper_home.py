# Завдання 5
# Користувач вводить текст і набір символів. Видаліть з тексту всі слова, що містять хоча б один з цих символів, і виведіть результат.

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ac efficitur urna. Duis ac porta lectus. Sed fermentum enim vitae ullamcorper dignissim. Praesent gravida congue mollis. Ut finibus elit vehicula mauris consectetur tempus. Donec et luctus leo. In vestibulum gravida ex at sagittis. Pellentesque convallis tincidunt finibus. Morbi justo elit, gravida vitae augue vitae, luctus volutpat tellus. Pellentesque nec erat lorem. Nulla tellus ex, eleifend non massa ut, molestie mollis diam. Proin vitae tempus odio. Proin vel viverra lorem. Aliquam auctor iaculis ipsum eu viverra."
symbol = "srlp"

import re
words = re.findall("[ ]*\w+[.,! ]*", text)
print(words)

for word in words:
    for s in symbol:
        if word.lower().find(s.lower()) != -1:
            text = text.replace(word,"")
            break
print(text)