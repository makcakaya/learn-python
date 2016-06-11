# sort method sorts and changes the list acoordingly
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() 
print(cars)
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:')
print(cars)

# sorted function takes a list and returns a sorted list without affecting the list parameter
print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)

# revers method reverses and changes the list accordingly
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# you can always call reverse method again to get the original list order
cars.reverse()
print(cars)
print("I have " + str(len(cars)) + " cars.") # len function returns the length of the given list