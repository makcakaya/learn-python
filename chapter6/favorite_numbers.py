favorite_numbers = {
    'mert': 7,
    'okan': 14,
    'joe': 44,
    'jack': 2
}

for name in favorite_numbers:
    print(name.title() + " loves number " 
        + str(favorite_numbers[name]) + "!")

# More than one favorite number
favorite_numbers = {
    'mert': ['7', '11', '14'],
    'okan': ['3', '4'],
    'joe': ['1', '100']
}

for name, numbers in favorite_numbers.items():
    print(name.title() + " likes following numbers:")
    for number in numbers:
        print(number)