#write a python program which will keep adding stream of numbers
#inputted by the user. The addition stops when the user presses the q button

def getItemsPrice(prices_of_items) -> None:
    print("Here is the list of items prices:")
    for index in range(len(prices_of_items)):
        print(f"{index+1}. {prices_of_items[index]}")

def addItems() -> None:
    sum = 0
    price_of_items = []
    while True:

            userInput = input("Enter the price: ")
            if userInput != "q":

                if userInput.isdigit():
                    sum += int(userInput)
                    price_of_items.append(userInput)
                    print(f"Total bill so far: {sum}")
                else:
                    print("Please enter a valid number.")

            else:
                break

    print("Thanks for shopping!")
    print(f"Your total bill is: {sum}")
    getItemsPrice(price_of_items)

addItems()



