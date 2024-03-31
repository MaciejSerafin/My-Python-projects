def add(*args):
    print(args[1])
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(2,3,4,5,6,7,8,9))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key, value)
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.year = kw.get("year")

my_car = Car(make="Nissan", model="GTR")
print(my_car.year)