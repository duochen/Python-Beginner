class Dog:
    def __init__(self, name, age):
        self.dog_name = name
        self.dog_age = age

    def sit(self):
        print(f"{self.dog_name} sits")

    def roll_over(self):
        print(f"{self.dog_name} roll over")

    

########################################

dog = Dog('Rocky', 3)
print(type(dog))
dog.sit()
dog.roll_over()

dog1 = Dog('Lucky', 6)
dog1.sit()
dog1.roll_over()