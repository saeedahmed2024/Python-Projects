import random
import string
from words import words

MAX_LIVES = 5

def choose_valid_word(words):
    while True:
        # choose a random word
        word = random.choice(words).upper()

        # check if this word is valid (no - or whitespace in between)
        if '-' not in  word and ' ' not in word:
            break
    return word

def display_underscores(word: string, list_of_letters = []):
    output_str = ""
    for letter in word:
        if letter in list_of_letters:
            output_str += f"{letter}  "
        else:
            output_str += "_  "

    return output_str

#take each individual letter as input from the user
def input_user_letter():
    while True:
        letter = input("Enter a letter: ").upper().strip()
        if (len(letter) == 1):
            break
        else:
            print("Please enter a single letter!")

    return letter


def is_word_formed(word_to_guess, correct_guesses):
    for letter in word_to_guess:
        if letter not in correct_guesses:
            return False
    return True

#validity check (input should not be repeated)
def check_letter_unique(letter, letters):
    return True if letter not in letters else False

#check if letter is in the chosen word
def check_letter_in_word_to_guess(letter, guessing_word):
    for index in range(len(guessing_word)):
        if guessing_word[index] == letter:
            return True

    #letter not found
    return False

def play_again():
    continue_game = input("Do you want to play again?(y/n): ").lower()
    if (continue_game == 'y'):
        main()
    else:
        exit(0)

def display_letters_guessed(letters):
    print("Letters you have already guessed: ")
    for letter in letters:
        print(letter, end= ", ")
    print()

def main():
    word_to_guess = choose_valid_word(words)
    display_underscores(word_to_guess)

    user_lives = MAX_LIVES
    user_guesses = []
    correct_guesses = []

    #repeat until user guesses the word or fails all the attempts
    while True:
        print(display_underscores(word_to_guess, correct_guesses))
        letter = input_user_letter()

        if check_letter_unique(letter, user_guesses):
            user_guesses.append(letter)

            if check_letter_in_word_to_guess(letter, word_to_guess):
                correct_guesses.append(letter)
                if is_word_formed(word_to_guess, correct_guesses):
                    print(display_underscores(word_to_guess, correct_guesses))
                    print("Congratulations! You have guessed the word correctly!")
                    break
            else:
                print("Oops! Wrong guess. (-1 lives)")
                user_lives-=1
                print(f"Remaining lives: {user_lives}")

            display_letters_guessed(user_guesses)
        else:
            print("Letter already chosen. Please select another letter")
        if user_lives == 0:
            print(f"You ran out of lives!\nThe correct answer was {word_to_guess}")
            break

    play_again()

main()





