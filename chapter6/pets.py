dost = {
    'type': 'dog',
    'owner': 'levent'
}

minnos = {
    'type': 'cat',
    'owner': 'selime'
}

cavus = {
    'type': 'bird',
    'owner': 'mert'
}

pets = [dost, minnos, cavus]

for pet in pets:
    print(pet['owner'].title() + " owns a " + pet['type'] + ".")