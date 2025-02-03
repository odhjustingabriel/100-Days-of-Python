import random

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 7

    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100. You have 7 attempts to guess it.")

    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")
        try:
            # Get the user's guess
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly!")
            return
        elif guess < secret_number:
            print("Too Low!")
        else:
            print("Too High!")

        # Decrement the number of attempts
        attempts -= 1

    # If the user runs out of attempts
    print(f"\nSorry, you've run out of attempts. The correct number was {secret_number}.")

number_guessing_game()