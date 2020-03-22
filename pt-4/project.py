import lala_framework as lala
import keyword as k
import random

# lala.printName('johnny')
# print(lala.user['name'])

# print(k.iskeyword('def'))
# print(k.kwlist)

# weather = random.random() * 150

# if weather <= 40:
#     print('its cold')
# elif weather <= 100:
#     print('its okay')
# else:
#     print('its hot')

# use __name__ to identify module where something is being called
# in python, when a module is imported, it is executed at runtime, unlike nodeJs
# __main__ is the top-level scope where your program executes
lala.printName('Johnny')
print(__name__)
