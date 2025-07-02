def main():
    # Example string
    example_string = "Hello, Python programmers!"

    # Iterate through the string and print each character
    print("Iterating through the string:")
    for char in example_string:
        print(char, end=' ')
    print()

    # Find and print the character with the minimum ASCII value in the string
    print("\nCharacter with the minimum ASCII value:")
    min_char = min(example_string)
    if min_char == ' ':
        print("Space (ASCII value: 32)")
    else:
        print(min_char)

    # Find and print the character with the maximum ASCII value in the string
    print("\nCharacter with the maximum ASCII value:")
    max_char = max(example_string)
    print(max_char)

    # Find and print the index of the first occurrence of 'o' in the string
    print("\nIndex of 'o':")
    index_o = example_string.index('o')
    print(index_o)

    # Convert the string into a list of characters and print the list
    print("\nConverting string to a list of characters:")
    list_of_chars = list(example_string)
    print(list_of_chars)

    # Count and print the number of occurrences of 'o' in the string
    print("\nCount of 'o' in the string:")
    count_o = example_string.count('o')
    print(count_o)

main()
# Displays the ASCII value and its character representation
min_ascii = 0