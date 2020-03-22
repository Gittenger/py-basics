# users = ['joe', 'cindy', 'billy', 'john', ["list2", 'johnny']]
# print(users[4][0])

# # use 'del' to delete
# del users[4][1]
# print(users)

# 'len' method for getting length
users = ['joe', 'cindy', 'billy', 'john']
# print(len(users))

# append adds to end
# users.append('david')

# insert adds at index
# users.insert(2, 'david')

# remove item, must match exactly, removes first match
# users.remove('billy')

# pop removes last index if no arg
# if arg (index), removes at index
# users.pop(2)

score = [1, 2, 2, 2, 3, 4]
# clear clears out the list
# score.clear()

# copy creates a copy
# newScore = score.copy()
# score[0] = 0

# setting to var, without copy, just creates a ref
# newScore = score
# score[0] = 0

# count counts occurrances
# print(score.count(2))

# index finds index of first occurrance
# print(score.index(4))


# sort
users.sort()
# print(users)

# reverse is reverse sort
score.reverse()
# print(score)


# BONUS
# similar to spread op
# called 'splatting' in python
old_list = [1, 2, 3]
old_list2 = [[4, 5]]
new_list = [*old_list, *old_list2]
# can also just do arr + arr
new_list = old_list + [6, 7]

print(new_list)
