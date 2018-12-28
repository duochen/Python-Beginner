class Car:
    def __init__(self, distance):
        self.distance = distance
    def drive(self, time):
        print("It takes {} hours".format(time))

car = Car(10)

try:
    speed = int(input("How fast?"))        
    time = car.distance / speed
    car.drive(time)
except ValueError as e:
    print(e)
except ZeroDivisionError:
    print("Division by zero!")
except (NameError, AttributeError):
    print("Bad Car")
except:
    print("Car unexpectedly crashed!")    


