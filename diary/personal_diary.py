# personal_diary.py

import os

def main():
    """
    This function collects a diary entry from the user and appends it
    to a file named 'diary.txt' at a specific absolute path.
    """

    # Prompt the user for the current date and time
    date_time = input("Enter the current date and time (e.g., July 21, 2025 - 12:30 PM): ")

    # Prompt the user for their diary entry
    entry = input("Write your diary entry: ")

    # Define the absolute path to the diary.txt file
    folder_path = r"C:\Users\bsherman\OneDrive - Ecker Center for Behavioral Health\Desktop\PythonADD100\diary"
    file_path = os.path.join(folder_path, "diary.txt")

    # Ensure the folder exists; create it if it doesn't
    os.makedirs(folder_path, exist_ok=True)

    # Open the file in append mode and write the entry
    try:
        with open(file_path, "a", encoding="utf-8") as diary_file:
            diary_file.write(f"{date_time}\n")
            diary_file.write(f"{entry}\n")
            diary_file.write("\n")  # Blank line to separate entries

        print(f"Your diary entry has been saved to:\n{file_path}")

    except Exception as e:
        print(f"An error occurred while saving your entry: {e}")

# Run the main function
if __name__ == "__main__":
    main()
# a custom list of characters. It generates and prints all possible two-letter combinations.