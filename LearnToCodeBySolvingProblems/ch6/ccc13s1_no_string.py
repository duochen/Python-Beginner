def is_distinct(year):
    """
    year is an integer year.

    Return True if year contains only distinct digits, False otherwise.
    """
    used = []
    while year > 0:
        digit = year % 10  # Obtain rightmost digit
        if digit in used:
            return False
        used.append(digit)
        year = year // 10  # Remove rightmost digit
    return True


year = int(input())

year = year + 1

while not is_distinct(year):
    year = year + 1

print(year)
