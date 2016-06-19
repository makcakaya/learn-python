vacations = {}

continue_poll = True
while continue_poll:
    name = input("What is your name? ")
    vacation = input("Where would you want to go? ")
    vacations[name] = vacation

    iterate = input("Would you like to make another turn? (yes/no) ")
    if iterate == 'no':
        continue_poll = False

for name, vacation in vacations.items():
    print(name.title() + " would like to visit " + vacation.title() + "!")
    
