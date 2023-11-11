def read(file):
    with open(file) as f:
        for line in f.readlines():
            yield line.split(',')
            
for line in read('input3.txt'):
    comp = {}
    for idx, num in enumerate(line):
        lst = [int(i) for i in num.strip()]
        if set(lst) == {1,3,4,6}:
            lst = [9,9,9,9]
        summ = sum(lst)
        sortlst = sorted(lst, reverse=True)
        comp[chr(idx+65)] = (summ, sortlst)
    maxim = max(comp.values(), key=lambda x:x[1])
    winers = [player for player in comp.keys() if comp[player] == maxim]
    print(''.join(winers))