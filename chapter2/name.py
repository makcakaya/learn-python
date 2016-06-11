''' title method converts the string so that each word starts with a capital
character and others are lower case character '''
name = "mert akcakaya"
weird_name = "HAm MocK"
print(name.title())
print(weird_name.title())

# string case change
print(name.upper())
print(name.lower())

# string concatenation
first_name = "mert"
last_name = "akcakaya"
full_name = first_name+ ' ' + last_name
message = "Hello, " + full_name.title() + "!"
print(message)

# Whitespace
print("Python")
print("\tPython")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping whitespace
favorite_language = 'Python   '
message = "I love " + favorite_language.rstrip() + "!"
print(message)

message = "   There were whitespaces around this sentence, now they're gone.   "
print(message.strip())