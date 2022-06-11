class Computer:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def describe(self):
        print(f"{self.make } {self.year}")

########################################

duo = Computer('Lenovo', 2018)
duo.describe()
michael = Computer('HP', 2004)
michael.describe()