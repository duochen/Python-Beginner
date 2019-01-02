def student(firstname, lastname = 'Mark', grade = 'Fifth'):
    print("First Name: ", firstname, " ", "Last Name: ", lastname, " ", "Grade: ", grade)

# 1 positional argument
student('John')             # => First Name:  John   Last Name:  Mark   Grade:  Fifth

# 2 positional arguments
student('John', 'Gates')    # => First Name:  John   Last Name:  Gates   Grade:  Fifth

# 3 positional arguments
student('John', 'Gates', 'Seventh') # => First Name:  John   Last Name:  Gates   Grade:  Seventh