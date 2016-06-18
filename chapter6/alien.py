alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying values

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

# Removing key-value pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

new_alien = {
    'color': 'black',
    'points': 1000,
    'weapons': ['laser gun', 'mind trick', 'energy pulse']
}

print("A new alien appeared. It is " + new_alien['color']
      + " and is worth " + str(new_alien['points']) + " because it has ")
for weapon in new_alien['weapons']:
    print(weapon.title())
print(' weapons!')