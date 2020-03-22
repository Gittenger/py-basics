user = {
    'fname': 'john',
    'lname': 'pittenger',
    'age': 29,
    'skills': ['HTML', 'CSS', 'Python'],
    'locations': ('Tenessee', 'Cincinnati', 'Cleveland'),
    'car': {
        'make': 'hyundai',
        'model': 'sonata',
        'year': '2015',
        'options': {
             'sunroof': True,
             'bluetooth': True,
             'remote_start': False
        }
    }
}

# use bracket notation to access values from keys
# print(user['car']['options']['remote_start'])

# use bracket notation to change fields
user['age'] = 30
print(user['age'])

# even though tuples are immutable, you can change the contents of...
# a list or a dictionary that is nested inside of a tuple
# but tuples themsleves don't support direct reassignment of their contents


# you can use del to remove a key from a dict
# dict.clear() will clear the entire dict
# len(dict) will tell you how many keys are in the dict at the first depth
# str(dict) will return a string rep of the dict
# check types using type(input)

# when assigning a dict to a var, it saves as reference
# use .copy() to create a copy

# dict.keys() will return list of keys (first level)
# dict.values() will return list of values

# you can add key/val pairs directly using bracket syntax

# dict.has_key() checks for a key, returns bool
