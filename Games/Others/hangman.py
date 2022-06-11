from random import *

player_score = 0
computer_score = 0

def start():
    print("Let's play a game of Hangman.")
    while game():
        pass
    scores()

def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player: ", player_score)
    print("Computer: ", computer_score)

def game():
    dictionary = ['elephant', 'houston', 'apple']
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score

    joinclue = "".join(clue)
    while (letters_wrong != tries) and (joinclue != word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:  # you enter the letter before
                print("You've already picked", letter)
            else:   # you enter a new letter
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:   # the user enters the wrong letter
                    letters_wrong += 1  # record the wrong times
                    print("Sorry,", letter, "isn't what we're looking for")
                else:    # the user enters the correct letter
                    print("Congratulations,", letter, "is correct.")
                    for i in range(word_length):
                        if letter == word[i]:     # find index of letter in word
                            clue[i] = letter      # replace _ with letter
        else: # the letter is not a character or more than one characters
            print("Choose another.")

        print(" ".join(clue)) # print _ with the correct letters
        print("Guesses:", letters_tried)

        if letters_wrong == tries:
            print("Game Over.")
            print("The word was", word)
            computer_score += 1
            break
        if "".join(clue) == word:
            print("You Win!")
            print("The word was ", word)
            player_score += 1
            break

    return play_again()

def play_again():
    answer = input("Would you like to play again? y/n: ")
    if answer in ('y', 'Y', 'yes', 'Yes', 'Of course!'):
        return answer
    else:
        print("Thank you very much for playing our game. See you next time!")
        
def guess_letter():
    print("")
    letter = input("Take a guess at our mystery word:")    
    letter.strip()
    letter.lower()
    print("")
    return letter

if __name__ == '__main__':
    start()    