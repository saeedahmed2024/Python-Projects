from typing import Dict, List
import string
import random

MAX_LINES = 3 #constants are defined using all capital letters
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}

symbols_value = {
    "A":5,
    "B":4,
    "C":3,
    "D":2,
}

def get_slot_machine_spin(rows: string, cols, symbols: dict[str, int]):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #copies the symbols list into current symbols

        for _ in range(rows):
            random_index = random.randint(0, len(current_symbols)-1)
            column.append(current_symbols[random_index])
            current_symbols.pop(random_index)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            print(column[row], end=" | " if i < len(columns) - 1 else "\n")

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol_to_check = columns[0][line]
        for column in columns:
            symbol = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += bet * values[symbol]
            winning_lines.append(line+1)

    return winnings, winning_lines





def deposit():
    while True:
        amount = input("What would you like to deposit?: $")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-"+str(MAX_LINES)+"): ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines")
        else:
            print("Please enter a number")

    return lines


def get_bet(deposit, lines):
    while True:
        amount = input("What would you like to bet on each line?: $")

        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}")
        else:
            print("Please enter a number")

    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet(balance, lines)
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough money to bet that amount. Your current balance is ${balance}")

        else:
            break

    balance-= total_bet

    print(f"You have bet ${bet} on {lines} lines. Your total bet is ${total_bet}.\nRemaining balance is ${balance}\n")
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)

    print(f"You won ${winnings}")
    print("You won on lines: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")

        if balance <= 0:
            print(f"You are out of balance.")
            break
        if input("Press Enter to play the game (q to quit): ").lower() == 'q':
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

main()


