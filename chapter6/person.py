person_0 = {
    'name': 'mert',
    'surname': 'akcakaya', 
    'age': 28,
    'instrument': 'drums'
}

print("Person's name is " + person_0['name'].title() + ".")
print("Person's surname is " + person_0['surname'].title() + ".")
print(person_0['name'].title() + " is " + str(person_0['age']) 
    + " years old.")
print(person_0['name'].title() + " can play " + person_0['instrument'] + ".")

person_1 = {
    'name': 'murat',
    'surname': 'deve',
    'age': 22,
    'instrument': 'guitar'
}

person_2 = {
    'name': 'deniz',
    'surname': 'cebel',
    'age': 32,
    'instrument': 'flute'
}


people = [person_0, person_1, person_2]

for person in people:
    print((person['name'] + " " + person['surname']).title() + " is "
          + str(person['age']) + " years old and plays " + person['instrument'] + ".")