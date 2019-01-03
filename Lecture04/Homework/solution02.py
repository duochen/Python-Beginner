sentence = 'Use a dictionary comprehension to count the length of each word in a sentence'
results = {word:len(word) for word in sentence.split()}
print(results) # => {'Use': 3, 'a': 1, 'dictionary': 10, 'comprehension': 13, 'to': 2, 'count': 5, 'the': 3, 'length': 6, 'of': 2, 'each': 4, 'word': 4, 'in': 2, 'sentence': 8}