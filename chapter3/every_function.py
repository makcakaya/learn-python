companies = ['google', 'microsoft', 'mozilla', 'apple']
print("There are " + str(len(companies)) + " number of companies in the list.")

companies.append('meltabi')
print(companies)
popped = companies.pop()
print(popped + " is out of the list.")

popped = companies.pop(2)
print(popped + " is a little different than others in the list.")

companies.append("oracle")
print(companies)

del companies[1]
print(companies)

print(sorted(companies))

companies.sort()
print(companies)
companies.reverse()
print(companies)

doomed = 'apple'
companies.remove(doomed)

print(companies)
print("The last item in the list is " + companies[-1].title() + '.') 