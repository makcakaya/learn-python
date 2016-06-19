active = True

while active:
    age = input("How old are you? ")
    
    if age == 'quit':
        break
    else:
        age = int(age)

    if age < 3:
        price = 0
    elif age < 12:
        price = 10
    else:
        price = 15
    
    if price == 0:
        print("It is free for you.")
    else:
        print("It will cost you " + str(price) + ".")
    
    # Close the theater if a zombie arrives
    if age == 100:
        active = False
        print("Sorry, but we're closed now.")
