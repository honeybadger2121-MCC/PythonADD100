import random

def main():
    # Generate a random number between 1 and 100
    numbers = list(range(1, 101))
    actual_number = random.choice(numbers)
    guessed_correctly = False

    while not guessed_correctly:
        # Get the user's guess
        guess = int(input("Enter your guess (between 1 and 100): "))

        # Calculate the difference between the guess and the actual number
        difference = abs(guess - actual_number)

        # Provide feedback based on the difference
        if difference == 0:
            print("Congratulations! You've guessed the correct number.")
            guessed_correctly = True
        elif difference <= 5:
            print("Very Hot")
        elif difference <= 15:
            print("Hot")
        elif difference <= 25:
            print("Cool")
        else:
            print("Cold")

if __name__ == "__main__":
    main()
# This code is a simple number guessing game where the user tries to guess a randomly selected number between 1 and 100.
# The user receives feedback based on how close their guess is to the actual number.