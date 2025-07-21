# Generator function to yield all possible two-letter combinations
def two_letter_combinations(characters):
    # Outer loop iterates over each character as the first letter
    for first in characters:
        # Inner loop iterates over each character as the second letter
        for second in characters:
            # Yield the combination of the two characters
            yield first + second

# Main function to interact with the user and print combinations
def main():
    # Preloaded list of characters
    default_list = ['x', 'y', 'z', 'u', 'v']

    # Ask the user if they want to use the default list or enter their own
    choice = input("Would you like to use the preloaded list of letters (x, y, z, u, v)? (yes/no): ").strip().lower()

    if choice == 'no':
        # Prompt the user to enter 5 letters
        user_input = input("Please enter 5 letters separated by spaces (e.g., a b c d e): ").strip().split()
        if len(user_input) != 5 or not all(len(char) == 1 and char.isalpha() for char in user_input):
            print("Invalid input. Using default list instead.")
            char_list = default_list
        else:
            char_list = user_input
    else:
        char_list = default_list

    # Call the generator function and print each combination
    print("\nTwo-letter combinations:")
    for combo in two_letter_combinations(char_list):
        print(combo)

# Run the main function
main()
# This code defines a generator function to yield all possible two-letter combinations
# from a given list of characters. It allows the user to either use a preloaded list