age = 28
print("Is my age 28? I think so.")
print(age == 28)

car = 'kia'
print("Is my car == 'kia'? I think so.")
print(car == 'kia')

sex = 'male'
print('Should print ' + str(True) + ' if I am male.')
print(sex == 'male')

isDeveloper = True
print('Am I a developer?')
print(isDeveloper == True)

isPythonFun = True
print('Is Python fun to work with?')
print(isPythonFun == True)

isPythonCompiled = False
print('Will I get an .exe from a Python program?')
print(isPythonCompiled)

isPythonFastest = False
print('Is Python the fastest executing programming language?')
print(isPythonFastest)

canBuildWebApp = True
print('Can I build only console application using Python?')
print(not canBuildWebApp)

hardToFindConditionalStatements = True
print('It must be so easy to find lots of conditional statements for testing, is not it?')
print(not hardToFindConditionalStatements)

lastConditional = True
print('This is not the last conditional for the first task, right?')
print(not lastConditional)

print("Is 'Mert' == 'mert'.title(): " + str('Mert' == 'mert'.title()))
print("Is 'mert' == 'Mert': " + str('mert' == 'Mert'))

print("Is 'MERT'.lower() == 'mert': " + str('MERT'.lower() == 'mert'))

guessNumber = 10
if guessNumber > 0 and guessNumber % 2 == 0:
    print("It is a positive even number.")
if guessNumber % 5 == 0 or guessNumber % 3 == 0:
    print("It is dividable by 5 or 3.")
if guessNumber < 100:
    print("It is less than a hundred.")
    if guessNumber <= 10:
        print("It is less than or equal to ten.")
        if guessNumber == 10:
            print("Nailed it, 10!")
        if guessNumber != 9:
            print("It is not 9 obviously")

eu = ['germany', 'england', 'italy', 'france']
print("Is Russia a part of EU? : " + str('Russia'.lower() in eu))
print("Is Germany a part of EU? : " + str('Germany'.lower() in eu))