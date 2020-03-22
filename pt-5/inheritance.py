class Vehicle():
    def __init__(self, wheels, windows, seats):
        self.wheels = wheels
        self.windows = windows
        self.seats = seats

    def printWheels(self):
        print(f"this vehicle has {self.wheels} wheels")
        return self.wheels


class Car(Vehicle):
    def __init__(self, make, model, wheels, windows, seats):
        super().__init__(wheels, windows, seats)
        self.model = model
        self.make = make

    def __repr__(self):
        return f"this is a car by {self.make}"


class Mcycle(Vehicle):
    def __init__(self, make, model, wheels, windows, seats):
        super().__init__(wheels, windows, seats)
        self.model = model
        self.make = make

    def __repr__(self):
        return f"this is a motorcycle by {self.make} with {self.printWheels()} wheels"


car1 = Car('benz', 'gl350', 4, 6, 5)
motor1 = Mcycle('benz', 'bike', 2, 1, 1)
# print(car1.printWheels())
# print(car1)
print(motor1)
