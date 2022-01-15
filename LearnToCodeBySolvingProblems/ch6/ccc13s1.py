def is_distinct(year):
    """
    year is an integer year.

    Return True if year contains only distinct digits, False otherwise.
    """
    # Convert to string and then check for duplicate characters.
    s = str(year)
    used = []
    for char in s:
        if char in used:
            return False
        used.append(char)
    return True


year = int(input())

year = year + 1

while not is_distinct(year):
    year = year + 1

print(year)
