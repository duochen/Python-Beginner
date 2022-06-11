from Car import Car, ElectricCar as EC

c = Car('audi', 'a4', 2019)
print(c.get_name())

e = EC('tesla', 'model x', 2020)
e.describe_battery()
