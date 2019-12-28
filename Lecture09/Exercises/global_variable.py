guesses = 0

def CheckGuess(aGuess):
    global guesses
    guesses = guesses + 1

aGuess = int(input('Please attempt a guess: '))
CheckGuess(aGuess)
print(guesses)