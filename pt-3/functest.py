# create list of random usernames
users = ['jim', 'joe', 'sally', 'virginia', 'alice', 'bob', 'zach', 'danny']

# function to print users


def print_users(users):
    for user in users:
        print(f"user_name: {user}")
    users.sort()
   # return sorted list of user names
    return users


print(print_users(users))
