lst = input().split()
k = int(lst[0])
n = int(lst[1])

letter_to_words = {}
letter_to_pos = {}

for i in range(k):
    word = input()
    letter = word[0]
    if not letter in letter_to_words:
        letter_to_words[letter] = [word]
        letter_to_pos[letter] = 0
    else:
        letter_to_words[letter].append(word)

for letter in letter_to_words:
    letter_to_words[letter].sort()

for i in range(n):
    letter = input()
    pos = letter_to_pos[letter]
    print(letter_to_words[letter][pos])
    num_words = len(letter_to_words[letter])
    letter_to_pos[letter] = (letter_to_pos[letter] + 1) % num_words
