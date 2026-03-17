import random


def play_game():
    # Generating a random secret number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Looping  until the user guesses correctly
    while True:
        try:
            #  Getting  the user's guess and convert to an integer
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Providing  feedback to the user
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You found the number in {attempts} attempts.")
                break  # Exit the loop when guessed correctly
        except ValueError:
            # Handle cases where the user types something other than a number
            print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    play_game()
