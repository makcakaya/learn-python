current_users = ['jack', 'joe', 'will', 'admin']

new_users = ['will', 'joe']

for user in new_users:
    if user.lower() in current_users:
        print("Username " + user + " is taken!")
    else:
        print("Username " + user + " is available.")