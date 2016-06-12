cubes = []
for value in range(1,11):
    cubes.append(value**3)
    print(cubes[-1])

# Using list comprehension
cubes = [value ** 3 for value in range(1,11)]
print(cubes)