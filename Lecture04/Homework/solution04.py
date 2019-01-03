numbers = [1,2,3,4,5,6]
results = [i for i in filter(lambda x:x>4, numbers)]
print(results)  # => [5, 6]