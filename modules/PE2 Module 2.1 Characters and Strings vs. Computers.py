def main():
    while True:
        # Prompt for user input
        user_input = input("Enter a single character: ")

        # Validate the input
        if len(user_input) != 1:
            print("Please enter exactly one character.")
            continue

        # Convert to ASCII value
        ascii_value = ord(user_input)
        print(f"The ASCII value of '{user_input}' is {ascii_value}.")

        break

    while True:
        try:
            # Prompt for ASCII value input
            ascii_input = int(input("Enter an ASCII value (32-127): "))

            # Validate the input
            if ascii_input < 32 or ascii_input > 127:
                print("Please enter a value between 32 and 127.")
                continue

            # Convert to character
            character = chr(ascii_input)
            print(f"The character for ASCII value {ascii_input} is '{character}'.")

            break
        except ValueError:
            print("Invalid input. Please enter a valid ASCII value.")

if __name__ == "__main__":
    main()
# This code prompts the user to enter a single character and then displays its ASCII value.
# It also allows the user to enter an ASCII value and displays the corresponding character.