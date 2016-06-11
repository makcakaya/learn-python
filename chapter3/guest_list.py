invited = ['Kadir', 'Mustafa', 'Ozgur']
print(invited[0] + ", please join me this evening at the dinner.")
print(invited[1] + ", I am waiting for you this evening for the dinner.")
print("I didn't forget you " + invited[2] + '!')

excused = 'Ozgur'
print("Unfortunately " + excused + " will not be with us this evening.")

invited.remove(excused)
new_person = 'lutfiye'
invited.insert(2, new_person.title())

print(invited[0] + ", please join me this evening at the dinner.")
print(invited[1] + ", I am waiting for you this evening for the dinner.")
print("I didn't forget you " + invited[2] + '!')

print("I have found a bigger table.")
first = 'ali'
middle = 'veli'
last = 'kamer'
invited.insert(0, first.title())
invited.insert(2, middle.title())
invited.append(last.title())
print("Welcome " + invited[0] + "!")
print("Welcome " + invited[1] + "!")
print("Welcome " + invited[2] + "!")
print("Welcome " + invited[3] + "!")
print("Welcome " + invited[4] + "!")
print("Welcome " + invited[5] + "!")

print("I have changed my mind and cannot stand you all at the same time!")
popped = invited.pop()
print("Sorry " + popped + ", but you are not welcome here!")
popped = invited.pop()
print("Sorry " + popped + ", but you too, please leave!")
popped = invited.pop()
print("Sorry " + popped + ", leave!")
popped = invited.pop()
print("Sorry " + popped + "!")
print(invited[0] + ", you please have a seat.")
print(invited[1] + ", you can take the seat next to him.")
print("There are " + str(len(invited)) + " guests tonight.")
del invited[1]
del invited[0]
print(invited)