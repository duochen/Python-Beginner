purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)  # => {'money': 12, 'candy': 3, 'tissues': 75}
print(purse['candy'])  # => 3
purse['candy'] = purse['candy'] + 2
print(purse)  # => {'money': 12, 'candy': 5, 'tissues': 75}