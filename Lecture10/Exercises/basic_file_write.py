filename = "new_test.txt"

with open(filename, "w") as file_object:
    file_object.write("hello world, again")
    file_object.write("... and again")