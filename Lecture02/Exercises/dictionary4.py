counts = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key]) # => chuck 1 fred 42 jan 100
print(counts.keys())   # => dict_keys(['chuck', 'fred', 'jan'])
print(counts.values()) # => dict_values([1, 42, 100])
