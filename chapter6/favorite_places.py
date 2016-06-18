favorite_places = {
    'mert': ['bangkok', 'san diego', 'bern'],
    'utku': ['istanbul'],
    'john': ['tokat', 'bodrum']
}

for person, places in favorite_places.items():
    print(person.title() + " likes these places:")
    for place in places:
        print("\t" + place.title())