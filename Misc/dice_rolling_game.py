import random


def dice_rolling_game():
    while True:
    #prompt
        user_input = input("Roll dice(y/n): ").lower()

        if user_input == "y":
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            list_die = (die1, die2)
            print (list_die)

        elif user_input == "n":
            print("Thank you for playing!")
            break

        else:
            print("Invalid input")
    return

def main():
    dice_rolling_game()

    return

main()
