output = []
for element in iterable:
    if predicate(element):
        output.append(element)
return output

[element for element in iterable
    if predicate(element)]
