class Auto:
    def __init__(self, realise_of_year=2020, producer=None, car_brand=None, car_mileage=0, fuel_consumption: float = None):
        self.realise_of_year = realise_of_year
        self.producer = producer
        self.car_brand = car_brand
        self.car_mileage = car_mileage
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return f'{self.realise_of_year}, {self.producer}, {self.car_brand}, {self.car_mileage}, {self.fuel_consumption}'
    __repr__ = __str__


class Lorry(Auto):
    def __init__(self, realise_of_year=2020, producer=None, car_brand=None, car_mileage=0, fuel_consumption: float = None, carrying_capacity: int = None):
        super().__init__(realise_of_year, producer, car_brand, car_mileage, fuel_consumption)
        self.carrying_capacity = carrying_capacity

class


car1 = Lorry(2024, 'Nissan', 'Nissan', 500, 100)
car2 = Sport(2023, 'Mercedes', 'Mercedes', 500, 100)

print(str(car1))
print(str(car2))