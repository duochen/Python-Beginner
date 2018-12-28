f = [1, True, [2, 3]]
str = " : ".join(str(x) for x in f)
print(str)

g = [0, 1, 0, 6, 'A', 1, 0, 7]
str1 = filter(lambda s: isinstance(s, int) == True and s > 0, g)
print(list(str1))