# absolute val
# print(abs(-20))

# min, max, convert to int/float
#
# numbers = [65, 87, 99, 100, 43, 2, 34, 12]
# print(f"min: {min(numbers)}")
# print(f"max: {max(numbers)}")
# grade = "93"
# print(type(grade))
# print(int(grade))
# grade = "93.24"
# print(float(grade))
# print(type(float(grade)))

# rounding, rounds to nearest, second arg is how many digits rounding to
# skip arg to round to whole num
# skills = 78.3456
# print(round(skills, 1))

# powers
# new = pow(2, 4)
# print(new)

# range function,
# numbers = range(10)
#    returns => range(0, 10)
# can be turned into list or tuple
# print(tuple(numbers))

# using filter
numbers = [65, 87, 99, 100, 43, 2, 34, 12,
           455, 634, 122, 120, 111, 1092, 248, 33, 45]


# def filterNum(number):
#     if(number > 100):
#         return True
#     else:
#         return False

# filter takes in a filter func, an iterable, and returns a filter obj
# you can then turn that filter obj into some iterable such as a list or tuple
# you can pass in a lambda as your filter function
# print(list(filter(lambda number: number > 1000, numbers)))


# map
# map returns a map obj, very similar to filter

# def vegetas(item):
#     return f"Vegeta's power level is {item}"


# afterMapLines =list(map(lambda item: f"Vegeta's power level is {item}", numbers))

for line in list(
        map(lambda item: f"Vegeta's power level is {item}", numbers)):
    print(line)
