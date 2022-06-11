class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def fill_gas(self):
        print("Fill gas")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = 75

    def describe_battery(self):
        print(f"Battery: {self.battery}")

    def fill_gas(self):
        print("Electric car doesn't use gas!")
