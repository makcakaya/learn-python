sandwich_orders = ['cheese', 'vegeterian', 'tuna', 'beef']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made you a " + sandwich + " sandwich!")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)

# Remove pastrami

sandwich_orders = ['cheese', 'pastrami', 'vegeterian', 'pastrami', 
                   'tuna', 'beef', 'pastrami']
finished_sandwiches = []

print("Deli has no more pastrami, sorry!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made you a " + sandwich + " sandwich!")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)