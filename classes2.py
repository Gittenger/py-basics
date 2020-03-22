
class Car:
    def __init__(self, make, model, wheels=4):
        self.make = make
        self.model = model
        self.wheels = wheels
        self.total = 5

# repr is used to create a custom representation of an instance of an object
    def __repr__(self):
        return f"Make: {self.make}, model: {self.model}, wheels: {self.wheels}"

    @classmethod
    def testing(cls):
        print('class=====')
        print(cls)
        print(cls.total)
        print('class=====')

    def printMake(self):
        return self.make

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

print(car1)
