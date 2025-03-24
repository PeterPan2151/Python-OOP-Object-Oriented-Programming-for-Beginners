class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self._year = year


my_car = Car('Porsche', '911 Car', 2020)

# Can be accessed, but we shouldnt.
print(my_car._year)

