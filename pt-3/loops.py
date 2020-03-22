# WHILE
#
# name = 'Joe Santos Garcia'
# number = 0
# while(number < len(name)):
#     print(f'number: {name[number]}')
#     number += 1

# FOR
# name = 'Joe Santos Garcia'
# users = ['joe', 'james', 'johnny']

# idnumber = 1
# for user in users:
#     print(f"id: {idnumber}, name: {user}")
#     idnumber += 1

# idnumber = 1
# data = {
#     'fname': 'john',
#     'lname': 'pittenger',
#     'id': 1234
# }

# data.items() will return list of tuples, key/value pairs
# for key, value in data.items():
#     print(f'key: {key}, value: {value}')


# using BREAK AND CONTINUE
# use break to end process
# # continue to skip condition
# users = ['joe', 'james', 'johnny', 'cindy']

# for user in users:
#     if user == 'james':
#         continue
#     print(user)


# using for loops with a RANGE
# users = ['joe', 'james', 'johnny', 'cindy']

# # by default, range increments by one every time
# # 3rd arg specifies increment amount
# for number in range(5, 101, 5):
#     print(number)


# using ELSE with loops
# add else at end of for loop to have some end condition when loop completes
print('welcome to itunes')
answer = input('do you want to download all your music? y/n')
if answer == 'y':
    for percent in range(1, 100):
        print(f'{percent}%')
    else:
        print("Download 100% complete!")
