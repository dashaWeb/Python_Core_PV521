directory = '18_files'

file_t = 'file.txt'
file_b = 'file.dat'
file_j = 'file.json'


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In volutpat faucibus scelerisque. Vestibulum fringilla nunc vitae porta lobortis. Vestibulum tincidunt vestibulum tellus eget molestie."

list_ = ["red", "green", "yellow", 'purple', "pink", "gold"]

item = {
    'name': 'program Python',
    'price': 9.5,
    'number': 18
}

group = [{
    "name": "Nona",
    "last_name": "Passie",
    "email": "npassie0@addthis.com",
    "date": "23/05/2008"
}, {
    "name": "Germain",
    "last_name": "Ventham",
    "email": "gventham1@merriam-webster.com",
    "date": "28/05/2001"
}, {
    "name": "Anthiathia",
    "last_name": "Hallbird",
    "email": "ahallbird2@bravesites.com",
    "date": "10/01/2010"
}, {
    "name": "Gabriellia",
    "last_name": "Elvy",
    "email": "gelvy3@netvibes.com",
    "date": "30/01/2003"
}, {
    "name": "Allistir",
    "last_name": "Iiannoni",
    "email": "aiiannoni4@xing.com",
    "date": "27/12/2001"
}, {
    "name": "Caterina",
    "last_name": "Chazette",
    "email": "cchazette5@vistaprint.com",
    "date": "12/10/2005"
}, {
    "name": "Timi",
    "last_name": "Dufall",
    "email": "tdufall6@t-online.de",
    "date": "12/07/2006"
}, {
    "name": "Taffy",
    "last_name": "Scryne",
    "email": "tscryne7@ameblo.jp",
    "date": "01/01/2001"
}, {
    "name": "Cecil",
    "last_name": "Gomery",
    "email": "cgomery8@aol.com",
    "date": "13/10/2000"
}, {
    "name": "Ricky",
    "last_name": "MacKnockiter",
    "email": "rmacknockiter9@buzzfeed.com",
    "date": "21/01/2009"
}]


# with open(f'{directory}/{file_t}', 'w') as file:
#     file.write(text)

# with open(f'{directory}/{file_t}', 'w') as file:
#     file.writelines(list_)

# with open(f'{directory}/{file_t}', 'w') as file:
#     file.writelines(item)

import pickle

# with open(f'{directory}/{file_b}', 'wb') as file:
#     # res = pickle.dumps(text)
#     # file.write(res)
#     pickle.dump(text,file)

# with open(f'{directory}/{file_b}', 'rb') as file:
#     # res = file.read()
#     # print(pickle.loads(res))
#     print(pickle.load(file))


# with open(f'{directory}/{file_b}', 'wb') as file:
#     pickle.dump(list_,file)

# with open(f'{directory}/{file_b}', 'rb') as file:
#     res = pickle.load(file)
#     print(type(res), res, "\n", res[2])


# with open(f'{directory}/{file_b}', 'wb') as file:
#     pickle.dump(item,file)

# with open(f'{directory}/{file_b}', 'rb') as file:
#     res = pickle.load(file)
#     print(type(res), res, "\n", res['name'])


# with open(f'{directory}/{file_b}', 'wb') as file:
#     pickle.dump(group,file)

# with open(f'{directory}/{file_b}', 'rb') as file:
#     res = pickle.load(file)
#     print(type(res), res, "\n", res[2]['name'])

# with open(f'{directory}/{file_b}', 'rb') as file:
#     students = pickle.load(file)

# new_st = {
#     "name": "Nona222222",
#     "last_name": "Passie222222",
#     "email": "npassie0@addthis.com222222",
#     "date": "23/05/20082222222"
# }

# students = list(students)
# students.append(new_st)
# print(students)

# with open(f'{directory}/{file_b}', 'wb') as file:
#    pickle.dump(students,file)

import requests
import json
response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
res = response.content
res = json.loads(res)
print(res)
# print(type(res), res, res[0]['buy'])


# with open(f'{directory}/{file_j}', 'w') as file:
#     json.dump(group, file)

# with open(f'{directory}/{file_j}', 'r') as file:
#     print(json.load(file))