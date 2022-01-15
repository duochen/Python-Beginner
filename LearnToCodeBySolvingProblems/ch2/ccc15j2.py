s = input()

happy_count = s.count(':-)')
sad_count = s.count(':-(')

if happy_count == 0 and sad_count == 0:
    print('none')
elif happy_count == sad_count:
    print('unsure')
elif happy_count > sad_count:
    print('happy')
else:
    print('sad')
