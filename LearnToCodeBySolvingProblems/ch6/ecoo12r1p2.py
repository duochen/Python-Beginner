PROMOTER = 'TATAAT'


def complement(s):
    """
    s is a string of DNA.

    Return a string: the complement of s.
    """
    result = ''
    for char in s:
        if char == 'A':
            result = result + 'T'
        elif char == 'T':
            result = result + 'A'
        elif char == 'C':
            result = result + 'G'
        else:
            result = result + 'C'
    return result


for dataset in range(5):
    strand = input()
    start = strand.index(PROMOTER) + 10
    i = start
    found = False
    while not found:
        j = i + 6
        piece = strand[i:j]
        # You could write a function to return the reverse of a string
        # It can also be done with string slicing, by adding a :-1
        piece_rev = piece[::-1]
        if complement(piece_rev) in strand[j:]:
            found = True
        else:
            i = i + 1

    rna = strand[start:i]
    rna = complement(rna)
    rna = rna.replace('T', 'U')

    print(f'{dataset+1}: {rna}')
