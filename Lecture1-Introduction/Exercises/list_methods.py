# Make a list
users = ['val', 'bob', 'mia', 'ron', 'ned']

# Get the element
first_user = users[0]       # first element
second_user = users[1]      # second element
newest_user = users[-1]     # last element

# Modify individual items
users[0] = 'valerie'        # change an element
users[-2] = 'ronald'
users.append('amy')         # add an element to the end of the list
users.insert(0, 'joe')      # insert an element at a particular position

# Remove elements 
del users[-1]               # delete an element by its position
users.remove('mia')         # remove an item by its value 

# Pop elements
most_recent_user = users.pop()  # pop the last item from a list
first_user = users.pop(0)       # pop the first item in a list

# List length
num_users = len(users)  	# find the length of a list

# Sort a list
users.sort()                 	# sort a list permanently
users.sort(reverse=True)   	    # sorting a list permanently in reverse  order
users.reverse()              	# reverse the order of a list
sorted(users)                	# sort a list temporarily 

# The range() function
for number in range(1001):            	
    print(number)			    # Print the numbers 0 to 1000 	

for number in range(1, 1001):
    print(number)               # Print the numbers 1 to 1000

numbers = list(range(1, 1000001))   # Make a list of numbers from 1 to a million

# Slice a list
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
first_three = finishers[:3]   		# Get the first three items
middle_three = finishers[1:4] 		# Get the middle three items
last_three = finishers[-3:]  		# Get the last three items

# List comprehensions
squares = []                  		# Using a loop to generate a list of square numbers
for x in range(1, 11):
    square = x**2
    squares.append(square)

squares = [x**2 for x in range(1, 11)]   		# Generate a list of square numbers

names = ['kai', 'abe', 'ada', 'gus', 'zoe']   	# Convert a list of names to upper case
upper_names = []
for name in names:
    upper_names.append(name.upper())

names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = [name.upper() for name in names]   # Convert a list of names to upper case

# Copy a list
finishers = ['kai', 'abe', 'ada', 'gus', 'zoe']
copy_of_finishers = finishers[:]                  # Make a copy of a list

# Build a list and print the items in the list
dogs = []
dogs.append('willie')
dogs.append('hootz')
dogs.append('peso')
dogs.append('goblin')
for dog in dogs:
    print("Hello " + dog + "!")
    print("I love these dogs!")
    print("\nThese were my first two dogs:")

old_dogs = dogs[:2]
for old_dog in old_dogs:
    print(old_dog)
del dogs[0]
dogs.remove('peso')
print(dogs)



# Simple statistics
ages = [93, 99, 66, 17, 85, 1, 35, 82, 2, 77]
youngest = min(ages)         # Find the minimum value 
oldest = max(ages)           # Find the maximum value
total_years = sum(ages)      # Find the sum of all values