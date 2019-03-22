# Import module hello
import hello

# Now you can call defined function that module as follows
hello.say_hello("Duo")  # => Hello! Duo

print(__name__)         # => __main__
print(hello.__name__)   # => hello