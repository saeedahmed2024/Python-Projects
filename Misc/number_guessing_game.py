import random

def main():

    number_to_guess = random.randint(1, 100)

    while True:

        try:
            user_input = int(input("guess the number between 1 and 100: "))

            if user_input>100 or user_input<1:
                print("Invalid number")

            elif user_input < number_to_guess:
                print("Too low.")

            elif user_input > number_to_guess:
                print("Too high.")

            else:
                print("Congratulations! You guessed the number.")
                break
        except ValueError:
            print("Please enter a valid number.")
    return

main()