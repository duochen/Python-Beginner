data = "cranes varsity bangalore"

unique = set(data)

print("Number of unique characters:", len(unique)) # => 15
print("List of unique characters: ", unique) # => {'b', 'y', 'n', 'g', 'v', 'c', 'i', 'o', 't', 's', ' ', 'a', 'e', 'r', 'l'}

data = list(data)
for item in unique:
    data.remove(item)

print("Repeated characters: ", set(data)) # => {'n', 's', ' ', 'a', 'e', 'r'}