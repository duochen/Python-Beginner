my_file = open("text.txt", "r")

for line in my_file:
    print(line)

# result = my_file.readlines()
# print(result)
# for line in result:
#     print(line)

# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

my_file.close()