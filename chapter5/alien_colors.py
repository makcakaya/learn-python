alien_colors = ['green', 'yellow', 'red']

for alien_color in alien_colors:
    if alien_color == 'green':
        points = 5
    elif alien_color == 'yellow':
        points = 10
    elif alien_color == 'red':
        points = 15

    print("You have earned " + str(points) + " points for shooting a " + alien_color + " alien.")