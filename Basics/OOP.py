# Ex 1
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


modelS = Vehicle(240, 18)
print(modelS.max_speed, modelS.mileage)
print('____________________________________')


# Ex 2
# class Vehicle:
#     pass


# Ex 3
class Vehicle:  # this should be inheritance

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


School_bus = Bus('School Volvo', 180, 18)
print('Vehicle Name:', School_bus.name, 'Speed: ', School_bus.max_speed, 'Mileage: ', School_bus.mileage)

print('____________________________________')


# Ex 4
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())

print('____________________________________')


# Ex 5
class Vehicle:
    color = 'white'  # default value in a class var

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


School_bus = Bus("School Volvo", 180, 12)
print('Color:', School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print('Color:', car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)
print('____________________________________')


# Ex 6
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        final_amount = super().fare()
        final_amount = final_amount + final_amount * 10 / 100
        return final_amount


School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

print('____________________________________')


# Ex 7
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)
print(type(School_bus))  # belongs to class Bus
print('____________________________________')


# Ex 8
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)
x = isinstance(School_bus, Vehicle)
print(x)

const numbers = [1, 2, 3];
numbers[5] = 11;
console.log(numbers);
