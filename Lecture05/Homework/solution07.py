try:
    x = 5 / 0
except ZeroDivisionError as e:
    # 'e' is the exception object
    print("Got a dvide by zero! The exception was:", e)
    # handle exceptional case
    x = 0
finally:
    print("The END")
    # it runs no matter what execute.

# Got a dvide by zero! The exception was: division by zero
# The END    