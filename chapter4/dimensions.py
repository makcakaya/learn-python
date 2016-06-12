dimensions = (200, 50)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# You can't change the elements in the tuple but you can change the
# tuple varible itself
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)