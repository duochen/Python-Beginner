class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open!")

my_restaurant = Restaurant("Duo's Cafe", "Chinese")        
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

