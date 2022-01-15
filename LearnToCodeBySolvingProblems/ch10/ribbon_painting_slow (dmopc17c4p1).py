# This solution is not efficient enough to pass all test cases in time.


lst = input().split()
n = int(lst[0])
q = int(lst[1])

blue_units = set()

for i in range(q):
    stroke = input().split()
    stroke_start = int(stroke[0])
    stroke_end = int(stroke[1])
    for stroke_unit in range(stroke_start, stroke_end):
        blue_units.add(stroke_unit)

print(n - len(blue_units), len(blue_units))
