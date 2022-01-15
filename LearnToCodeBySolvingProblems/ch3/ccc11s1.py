n = int(input())

count_s = 0
count_t = 0

for i in range(n):
    line = input()
    count_s = count_s + line.count('s') + line.count('S')
    count_t = count_t + line.count('t') + line.count('T')

if count_t > count_s:
    print('English')
else:
    print('French')
