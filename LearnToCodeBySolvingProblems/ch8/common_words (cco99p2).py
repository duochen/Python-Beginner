def invert_dictionary(d):
    """
    d is a dictionary mapping strings to numbers.

    Return the inverted dictionary of d.
    """
    inverted = {}
    for key in d:
        num = d[key]
        if not num in inverted:
            inverted[num] = [key]
        else:
            inverted[num].append(key)
    return inverted


def with_suffix(num):
    """
    num is an integer >= 1.

    Return a string of num with its suffix added; e.g. '5th'.
    """
    s = str(num)
    if s[-1] == '1' and s[-2:] != '11':
        return s + 'st'
    elif s[-1] == '2' and s[-2:] != '12':
        return s + 'nd'
    elif s[-1] == '3' and s[-2:] != '13':
        return s + 'rd'
    else:
        return s + 'th'


def most_common_words(num_to_words, k):
    """
    num_to_words is a dictionary mapping number of occurrences to
        lists of words.
    k is an integer >= 1.

    Return a list of the kth most-common words in num_to_words.
    """
    nums = list(num_to_words.keys())
    nums.sort(reverse=True)

    total = 0
    i = 0
    done = False
    while i < len(nums) and not done:
        num = nums[i]
        if total + len(num_to_words[num]) >= k:
            done = True
        else:
            total = total + len(num_to_words[num])
            i = i + 1

    if total == k - 1 and i < len(nums):
        return num_to_words[nums[i]]
    else:
        return []


n = int(input())

for dataset in range(n):
    lst = input().split()
    m = int(lst[0])
    k = int(lst[1])

    word_to_num = {}

    for i in range(m):
        word = input()
        if not word in word_to_num:
            word_to_num[word] = 1
        else:
            word_to_num[word] = word_to_num[word] + 1

    num_to_words = invert_dictionary(word_to_num)

    ordinal = with_suffix(k)
    words = most_common_words(num_to_words, k)

    print(f'{ordinal} most common word(s):')
    for word in words:
        print(word)

    print()
