numberList = [1, 2, 3]
strList = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting iterator to list
resultList = list(result)
print(resultList)

# Two iterables are passed
result = zip(numberList, strList)

# Converting iterator to set
resultSet = set(result)
print(resultSet)

result = zip(strList)
resultList = list(result)
print(resultList)