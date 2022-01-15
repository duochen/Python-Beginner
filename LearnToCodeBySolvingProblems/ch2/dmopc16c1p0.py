w = int(input())
c = int(input())

if w == 3 and c >= 95:
    word = 'absolutely'
elif w == 1 and c <= 50:
    word = 'fairly'
else:
    word = 'very'

print('C.C. is', word, 'satisfied with her pizza.')
