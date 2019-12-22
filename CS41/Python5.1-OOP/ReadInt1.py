def read_int():
    """Reads an integer from the user (broken)"""
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops! Invalid input. Try again...")
    return x

i = read_int()
print(i)