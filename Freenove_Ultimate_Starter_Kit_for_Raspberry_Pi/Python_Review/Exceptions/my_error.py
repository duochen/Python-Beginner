# Creates a class that inherits from the base Exception class
class MyError(Exception):
    pass

try:
    raise MyError("Some information about what went wrong")        
except MyError as error:
    print("Situation:", error)
