# BASICS
#
# # instantiate list class
# users = list()
# # use class method
# users.append('Joe')
# print(users)

# # use help method to show class
# help(users)
#


class Car:
    def __init__(self, make, model, wheels=4):
        self.make = make
        self.model = model
        self.wheels = wheels
        self.total = 5
        print(
            f'created instance of car for {make} {model} with {wheels} wheels')

    @classmethod
    # when using class methods, first param will be the class itself
    # use that to access class attributes
    # on instance methods, first param is by convention "self" which refers to the instance
    def testing(cls):
        print('class=====')
        print(cls)
        print(cls.total)
        print('class=====')

    def printMake(self):
        print('instance=====')
        print(self)
        print(Car.testing())
        print('instance=====')
        # return self.make

    def add(self, total):
        self.total += total
        Car.total += total
        return f"class-attribute: {Car.total} instance-attribute: {self.total}"

    total = 20


car1 = Car("benz", "ml350")
# car2 = Car("honda", "civic")
# car3 = Car("toyota", "corolla")
# car4 = Car("ford", "escape")
# car5 = Car("kenworth", "bigrig", 18)
# print(type(car1))
# print(car1.printMake())

# print(car1.add(5))
print(Car.testing())
# print(car1.printMake())
