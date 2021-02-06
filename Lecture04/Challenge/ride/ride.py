"""
ID: duochen2
LANG: PYTHON3
TASK: ride
"""

fin = open("ride.in", "r")
fout = open("ride.out", "w")

def multi(_list):
    res = 1
    # Calculate multiplication
    for x in _list:
        res *= x
    res %= 47
    return res

# Get representation of each letter, e.g, 'A' = 1, 'C' = 3
sums = [[ord(c) - 64 for c in line.strip()] for line in fin.readlines()]
sums = [multi(x) for x in sums]
fout.write ("GO\n" if sums[0] == sums[1] else "STAY\n")