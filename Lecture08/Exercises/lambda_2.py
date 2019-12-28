names = ['Magda', 'Jose', 'Anne']
lengths = []
for name in names:
    lengths.append(len(name))

print(lengths)

lengths = list(map(len, names))
print(lengths)