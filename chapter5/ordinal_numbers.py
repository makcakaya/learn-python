numbers = range(1,10)
for number in numbers:
    if number == 1:
        postfix = "st"
    elif number == 2:
        postfix = "nd"
    elif number == 3:
        postfix = "rd"
    else:
        postfix = "th"
    
    print(str(number) + postfix)