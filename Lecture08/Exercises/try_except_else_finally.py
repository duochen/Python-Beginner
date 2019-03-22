try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
except ValueError:
    print("You should have given either an int or a float.")    
except ZeroDivisionError:
    print("Infinity")
finally:
    print("There may or may not have been an exception.")