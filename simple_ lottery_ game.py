# Simple lottery game
import random

def lottery_game():
    # Function to generate winning numbers
    winning_numbers = random.sample
    (range(1, 50), 6)

    # Get user input
    user_numbers = []
    for i in range(6):
        while True:
            try:
                num = int(input(f"Enter number {i +  1}(1-49):"))
                if 1 <= num <= 49 and num not in user_numbers:
                    user_numbers.append(num)
                    break
                else:
                    print("Invalid input or number already chosen. Try again.")
            except ValueError:
                    print("Invalid input, Enter a valid number")

    # Compare user numbers with winning numbers
    matching_numbers = set(user_numbers).intersection(winning_numbers)

    # Display results
    print("\nWinning Numbers:", winning_numbers)
    print("Your numbers:", user_numbers)

    if len(matching_numbers) == 0:
       print("Sorry, you didn't get any numbers right.")
    else:
       print(f"Congratulations! You got {len(matching_numbers)}number(s)right; matching_numbers")

# Run the Game
lottery_game()