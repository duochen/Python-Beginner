output = []
for element in iterable:
    val = function(element)
    output.append(val)
return output

return [function(element) 
    for element in iterable]

map(fn, iter)

