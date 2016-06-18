cities = {
    'tokat': {
        'country': 'turkey',
        'population': 150000,
        'fact': 'best food'
    },
    'istanbul': {
        'country': 'turkey',
        'population': 20000000,
        'fact': 'corrupted megacity'
    },
    'munich': {
        'country': 'germany',
        'population': 1500000,
        'fact': 'largest city in Bavaria'
    }
}

for city, info in cities.items():
    print(city.title() + " is in " + info['country'].title()
          + " with a popluation of " + str(info['population'])
          + " and is known with " + info['fact'] + ".")