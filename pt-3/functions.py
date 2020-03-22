# BASIC FUNCTION DEFS
# def sum_up(a, b=2):
#     total = a + b
#     total += 1
#     total *= 2
#     return total


# def print_user(fname, lname, age):
#     print(f'{fname} {lname} is {age} years old')
#     return [fname, lname, age]


# print(print_user('john', 'pittenger', sum_up(3)))


# LAMBDA FUNCS..
# regular function is...
def add_up(a, b):
    return a + b


# lambda is an anonymous function assigned to a variable
# useful for returning functions
def sumUp(a, b): return a + b
# print(sumUp(2, 2))


def func(a):
    return lambda b: a * b


doubleUp = func(2)

print(doubleUp(10))
