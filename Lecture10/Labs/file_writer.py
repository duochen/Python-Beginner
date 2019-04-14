filename = "file_writer.txt"

with open(filename, "w") as file_object:
    for i in range(1,5):
        file_object.write("hello world, again")
        file_object.write("... and again")

print("Done")