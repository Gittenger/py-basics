# age = 20
# age *= 4

# alternative ways to declare vars
age, name, location = 29, 'John', 'Ohio'
a = b = c = 1

print(age, name, location)
print(a, b, c)


# in python, variables can always be changed. there aren't "constants"
# convention is, variable name in ALLCAPS means it should be treated as a const

# most devs use snake_case when declaring var names, instead of camel case

# "dunder" == double underscores
# __var_name__  == this means don't change this variable. super "const"


# concept of NULL
total_score = None
print(total_score)
# None == null, must be typed with capital case


username = input("What's your name? ")
user_location = input('Where do you live? ')
user_age = input('How old are you? ')

print(f"{username} is {user_age} years old and lives in {user_location}")
