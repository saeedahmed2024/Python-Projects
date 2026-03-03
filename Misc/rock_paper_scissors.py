import random
#we are able to implement DRY principle this way
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {ROCK : '🪨', 'p' : '📃', SCISSORS : '✂️'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper or Scissors? (r/p/s): ").lower()

        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice.")

def display_choices(user_choice, computer_choice):
    print("Computer chose: ", emojis[computer_choice])
    print("You chose: ", emojis[user_choice])

def determine_winner(user_choice, computer_choice):
    if ((user_choice == ROCK and computer_choice == SCISSORS) or
            (user_choice == PAPER and computer_choice == ROCK) or
            (user_choice == SCISSORS and computer_choice == PAPER)):
        print("You win!")

    elif ((user_choice == ROCK and computer_choice == PAPER) or
          (user_choice == SCISSORS and computer_choice == ROCK) or
          (user_choice == PAPER and computer_choice == SCISSORS)):
        print("You lose!")

    else:
        print("Draw!")

def play_game():
    while True:
        computer_choice = random.choice(choices)
        user_choice = get_user_choice()

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        continue_game = input('Continue? (y/n): ').lower()

        if continue_game == "n":
            break
    return

play_game()
