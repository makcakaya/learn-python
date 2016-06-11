motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'kawasaki'
print(motorcycles)
motorcycles[0] = 'honda'

motorcycles.append('ducati')
print(motorcycles)

motorcycles = [] # Make new list

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# insert method inserts the element at a specific position in the list
motorcycles.insert(0, 'ducati')
motorcycles.insert(-2, 'bmw')
print(motorcycles)

# del statement removes an element from a list if you know the position of the element
del motorcycles[0]
print(motorcycles)

# pop method removes an item from the list and returns the removed element
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped = motorcycles.pop()
print(motorcycles)
print(popped.title() + " is removed from the motorcycles list.")

first_owned = motorcycles.pop(0)
print(motorcycles)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# remove method removes the element with a given value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")