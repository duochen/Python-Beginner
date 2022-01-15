ADRIAN = 'ABC'
BRUNO = 'BABC'
GORAN = 'CCAABB'


n = int(input())
exam = input()

adrian_count = 0
bruno_count = 0
goran_count = 0

for i in range(len(exam)):
    if exam[i] == ADRIAN[i % len(ADRIAN)]:
        adrian_count = adrian_count + 1
    if exam[i] == BRUNO[i % len(BRUNO)]:
        bruno_count = bruno_count + 1
    if exam[i] == GORAN[i % len(GORAN)]:
        goran_count = goran_count + 1

most = adrian_count
if bruno_count > most:
    most = bruno_count
if goran_count > most:
    most = goran_count

print(most)

if adrian_count == most:
    print('Adrian')
if bruno_count == most:
    print('Bruno')
if goran_count == most:
    print('Goran')
