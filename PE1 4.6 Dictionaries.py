# Create the NATO Phonetic Alphabet dictionary
nato_alphabet = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot",
    "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima",
    "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo",
    "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee", "Z": "Zulu"
}

# Function to spell a word using the NATO Phonetic Alphabet
def spell_word():
    word = input("Enter a word: ").upper()  # Convert input to uppercase
    for letter in word:
        print(f"{letter}: {nato_alphabet.get(letter, 'Not found in NATO alphabet')}")  # Get phonetic value

# Main function to organize logic
def main():
    spell_word()

# Run the program
if __name__ == "__main__":
    main()
