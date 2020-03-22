# syntax error
# for x in names
#     print(x)

# # undefined
# for x in names:
#     print(x)

# raising custom errors
# you can set the error "type"
# check this link for more info on errors and error types
# https://www.programiz.com/python-programming/exceptions
#
# names = ['john', 23, {'test': 'jimmy'}]

# if len(names) <= 1:
#     raise Exception("Expecting more than one name")
# for x in names:
#     if type(x) is not str:
#         raise TypeError('The list contains an item which is not a string')
#     print(x)


def addUp(a, b):
    if (type(a) is not int) or (type(b) is not int):
        raise TypeError(
            'sorry, both arguments to the function must be of type Int')
    if a <= 0 or b <= 0:
        raise ValueError('args a or b are less than or equal to zero')
    return a + b


score = None

try:
    score = addUp(2, 3)
    
except (ValueError, TypeError) as error:
    print(error)
except:
    print('sorry there was an error')
else:
    print(f'score: {score}')
finally:
    print('calculation complete.....')
