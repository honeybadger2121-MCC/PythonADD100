# Custom iterator class for two-letter combinations
class TwoLetterCombinations:
    def __init__(self, characters):
        self.characters = characters
        self.i = 0  # Index for the first character
        self.j = 0  # Index for the second character
    def __iter__(self):
        # Return the iterator object itself
        return self
    def __next__(self):
        # If we've exhausted all combinations, stop iteration
        if self.i >= len(self.characters):
            raise StopIteration
        # Get the current combination
        combo = self.characters[self.i] + self.characters[self.j]

        # Move to the next second character
        self.j += 1

        # If we've reached the end of the second character list, move to the next first character
        if self.j >= len(self.characters):
            self.j = 0
            self.i += 1

        return combo

# Main function to interact with the user and print combinations
def main():
    default_list = ['x', 'y', 'z', 'u', 'v']

    choice = input("Would you like to use the preloaded list of letters (x, y, z, u, v)? (yes/no): ").strip().lower()

    if choice == 'no':
        user_input = input("Please enter 5 letters separated by spaces (e.g., a b c d e): ").strip().split()
        if len(user_input) != 5 or not all(len(char) == 1 and char.isalpha() for char in user_input):
            print("Invalid input. Using default list instead.")
            char_list = default_list
        else:
            char_list = user_input
    else:
        char_list = default_list

    print("\nTwo-letter combinations:")
    combinations = TwoLetterCombinations(char_list)
    for combo in combinations:
        print(combo)

# Run the main function
main()
# This code defines a custom iterator class for generating two-letter combinations
# from a list of characters. The user can choose to use a preloaded list or input