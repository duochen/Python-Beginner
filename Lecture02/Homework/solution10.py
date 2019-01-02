my_file = open("output.txt", "r+")
line = "Welcome to robotics time."
my_file.write(line)

# Move the stream position to the begining of the file
my_file.seek(0)

print(my_file.read())  # => Welcome to robotics time.
my_file.close()
