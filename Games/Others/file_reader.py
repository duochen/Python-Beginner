filepath = "pi_digits.txt"
with open(filepath, 'r') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)