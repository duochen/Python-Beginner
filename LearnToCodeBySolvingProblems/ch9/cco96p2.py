DIGITS = '0123456789'


# A guess is a list of three values: a code string of four digits,
# the number of correct digits, and the number of misplaced digits


def guess_consistent(number, code, correct, misplaced):
    """
    number is a string of four digits.
    code is the four-digit code of the guess.
    correct is the number of correct digits in the guess.
    misplaced is the number of misplaced digits in the guess.

    Return True if number is consistent with the guess, False otherwise.
    """
    number = list(number)
    code = list(code)
    num_correct = 0
    num_misplaced = 0

    # Determine number of correct digits
    for i in range(len(number)):
        if number[i] == code[i]:
            num_correct = num_correct + 1
            number[i] = ''
            code[i] = ''

    # Determine number of misplaced digits
    for i in range(len(number)):
        if number[i] != '' and number[i] in code:
            where = code.index(number[i])
            code[where] = ''
            num_misplaced = num_misplaced + 1

    return correct == num_correct and misplaced == num_misplaced


def all_guesses_consistent(number, guesses):
    """
    number is a string of four digits.
    guesses is a list of guesses.

    Return True if number is consistent with all guesses, False otherwise.
    """
    for guess in guesses:
        code = guess[0]
        correct = guess[1]
        misplaced = guess[2]
        if not guess_consistent(number, code, correct, misplaced):
            return False
    return True


def correctness_string(guesses):
    """
    guesses is a list of guesses.

    Return correct output string for guesses.
    """
    num_consistent = 0
    for digit1 in DIGITS:
        for digit2 in DIGITS:
            for digit3 in DIGITS:
                for digit4 in DIGITS:
                    number = digit1 + digit2 + digit3 + digit4
                    if all_guesses_consistent(number, guesses):
                        answer = number
                        num_consistent = num_consistent + 1
                        if num_consistent > 1:
                            return 'indeterminate'
    if num_consistent == 0:
        return 'impossible'
    else:
        return answer


n = int(input())

for dataset in range(n):
    num_guesses = int(input())
    guesses = []
    for i in range(num_guesses):
        line = input()
        code = line[:4]
        correct = int(line[5])
        misplaced = int(line[7])
        guesses.append([code, correct, misplaced])

    print(correctness_string(guesses))
