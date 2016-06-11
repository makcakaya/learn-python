bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())
print(bicycles[1].title())
# Index -1 is special, it is the index of the last item in the list
print(bicycles[-1].title())
print(bicycles[-2].title()) # Gets the second last item in the list

message = "My first bike was a " + bicycles[0].title() + "."
print(message)