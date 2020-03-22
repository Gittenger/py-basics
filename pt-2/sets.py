# sets are unordered lists, and you can't access their contents with bracket syntax
names = {'John', 'Cindy', 'Joe'}

# for x in names:
#     print(x)

names.add('James')
names.update(['sally', 'sue'])


names.remove('John')

for x in names:
    print(x)

print(len(names))

# use clear to clear a set
names.clear()
print(names)
# returns set()
#
print(len(names))
