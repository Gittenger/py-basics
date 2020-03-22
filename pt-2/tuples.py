users = ('Joe', 'Billy', 'Cindy', 'Josh')
schools = ('UC', 'UA')
# tuples are immutable
# users[1] = 'John' returns error

total = users + schools

# (item in tuple) returns bool
# print('UC' in total)

# you can use 'len' and 'del' on tuples too

# you can use the tuple() method to convert a list to a tuple
my_list = [1, 2, 3]
my_tuple = tuple(my_list) + schools
print(my_tuple)
