# personal_diary.py

def main():
    """
    This function prompts the user to enter the current date and time,
    along with a diary entry, and appends it to a file named diary.txt.
    Each entry is separated by a blank line for readability.
    """

    # Prompt the user for date and time
    date_time = input("Enter the current date and time (e.g., July 21, 2025 - 12:30 PM): ")

    # Prompt the user for their diary entry
    entry = input("Write your diary entry: ")

    try:
        # Open or create diary.txt in append mode
        with open("diary.txt", "a") as diary_file:
            # Write the date/time and entry to the file
            diary_file.write(f"{date_time}\n")
            diary_file.write(f"{entry}\n")
            diary_file.write("\n")  # Blank line to separate entries

        print("Your diary entry has been saved successfully.")

    except Exception as e:
        print(f"An error occurred while saving your entry: {e}")

# Run the main function
if __name__ == "__main__":
    main()
# a custom list of characters to generate combinations.