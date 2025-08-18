
stud = {
    'name':'Ivan',
    'surname':'Melnyk',
    'age':16,
    'marks':[10,11,9,8,12],
    'date':{
        'day':24,
        'month':3,
        'year':2000
    }
}

print(stud['name'])
print(stud.get('surname'))


# print(stud['name2'])
# print(stud.get('surname2'))
stud['name'] = 'Pavlo'
print(stud['name'])
stud['group'] = 'PV521'

print(stud)

def printStudent(student):
    print(f"Name    :: {student['name']}")
    print(f"Surname :: {student['surname']}")
    print(f"Age     :: {student.get('age')}")
    print(f"Marks   :: {', '.join(map(lambda x:str(x),student['marks']))}")
    print(f"Date    :: {'/'.join(map(lambda x: str(x), student['date'].values()))}")
    print(f"Group   :: {student.get('group')}")

printStudent(stud)

for key in stud.keys():
    print(key)
for val in stud.values():
    print(val)

for key, val in stud.items():
    print(key, val)

# del stud['group']
# printStudent(stud)
# stud.pop('age')
# printStudent(stud)
# deleted = stud.popitem()
# printStudent(stud)
# print(deleted)

clone = stud.copy()

print('Origin :: Student')
printStudent(stud)
print()
print('Clone :: Student')
printStudent(clone)
print()

clone['name'] = 'Denis'
clone['marks'] = stud['marks'].copy()
clone['marks'][0] = 333
print('Origin :: Student')
printStudent(stud)
print()
print('Clone :: Student')
printStudent(clone)
print()

new_stud = {}.fromkeys(clone.keys())
new_stud = {}.fromkeys(['red',1,5.4])
print(new_stud)


group = [
    {
        'name':'Ivan',
        'age':25
    },
    {
        'name':'Denis',
        'age':17
    },
    {
        'name':'alex',
        'age':21
    },
    {
        'name':'Pavlo',
        'age':15
    },
]

for students in group:
    for key, val in students.items():
        print(key,val, end="\t")
    print()

print()
group = sorted(group,key=lambda x: x['age'], reverse=True)
for students in group:
    for key, val in students.items():
        print(key,val, end="\t")
    print()

print(sorted(group, key= lambda x : x['name'].upper()))

print(list(filter(lambda x: x['age'] >= 18, group)))

def upAge(obj):
    obj['age'] += 1
    return obj
print(list(map(lambda x: dict(age=x['age'] + 1, name=x['name']), group)))
print(list(map(upAge, group)))