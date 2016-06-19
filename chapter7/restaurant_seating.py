seats = input("How many are you? ")
seats = int(seats)

if seats > 8:
    print("You'll have to wait.")
else:
    print("We have a table for " + str(seats) + " available right now.")