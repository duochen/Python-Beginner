def clean(address):
    """
    address is a string email address.

    Return cleaned address.
    """
    # Remove from '+' up to but not including '@'
    plus_index = address.find('+')
    if plus_index != -1:
        at_index = address.find('@')
        address = address[:plus_index] + address[at_index:]

    # Remove dots before @ symbol
    at_index = address.find('@')
    before_at = ''
    i = 0
    while i < at_index:
        if address[i] != '.':
            before_at = before_at + address[i]
        i = i + 1

    cleaned = before_at + address[at_index:]

    # Convert to lowercase
    cleaned = cleaned.lower()

    return cleaned


# Main Program

for dataset in range(10):
    n = int(input())
    addresses = set()
    for i in range(n):
        address = input()
        address = clean(address)
        addresses.add(address)

    print(len(addresses))
