# Assume we have the following list of tuples. We want to know how many red spins 
# separate a black spin, on average. We need a function which will yield the count 
# of gaps as it examines the spins. We can then call this function repeatedly to get 
# the gap information.

spins = [('red', '18'), ('black', '13'), ('red', '7'), 
    ('red', '5'), ('black', '13'), ('red', '25'), 
    ('red', '9'), ('black', '26'), ('black', '15'), 
    ('black', '20'), ('black', '31'), ('red', '3')]

def countReds(aList):
    count = 0
    for color, number in aList:
        if color == 'black':
            yield count
            count = 0
        else:
            count += 1
    yield count

gaps = [gap for gap in countReds(spins)]    
print(gaps)