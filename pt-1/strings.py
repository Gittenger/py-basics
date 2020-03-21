"Hi my name is John"
'Hi my name is John'
"Don't wrap string in single quotes if using single quotes inside of string"
# sentence = 'Hi my name is John'
# print(sentence)

# \n  is new line character
# 'Hi my name is \nJohn'


# \ can be used to escape chars
# use two \\ to show backslash
# to use emoji... \U(replace + with 000)Ucode
# "\"Don\'t wrap string in single quotes if using \\single quotes inside of string\" ~John Pittenger... \U0001F642"


# Concatenating strings
# use +
# sent = "Hello my name is"
# name = "John"
# print(sent + ' ' + name)


# get char of string
# myStr = 'hello'
# print(myStr[4])
# # get range of chars
# print(myStr[2:5])

# checking for chars in str
# case sensitive
# sent = 'hello my name is John'
# print('J' in sent)
# print('j' in sent)

# # you can use multiply operator on strings
# print('string' * 3)


# use mod operator with 's' (%s) in strings to do format operations in strings
# name = "john"
# city = "cincy"
# sentence = "hi my name is %s and I live in %s, %s" % (name, city, 'ohio')
# print(sentence)


# for string interpolation just use {var_name} inside string,
# must use 'f' at start of string
# You can place expressions inside curly braces

name = "johnnnny"
city = "cincy"
state = "ohio"
sentence = f"hi my name is {name[0:4]} and I live in {'.' * 4} {city}, {state +', ' + state}"
print(sentence)
