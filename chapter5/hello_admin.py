# usernames = ['jack', 'joe', 'will', 'admin']
usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to take the site down?")
        else:
            print("Hello " + username + ", you're logged in.")
else:
    print("We need to find some users!")