def replace_artist(top_artists):
    try:
        # Ask the user for the index of the artist to replace
        index = int(input("Enter the index of the artist to replace (0-9): "))
        
        # Ask the user for the new artist name
        new_artist = input("Enter the new artist name: ")
        
        # Replace the artist at the specified index
        top_artists[index] = new_artist
        
    except (ValueError, IndexError):
        # Handle both ValueError and IndexError with a general error message
        print("An input error occurred. Please enter a valid index and artist name.")
    else:
        # Display the updated list if no exceptions occur
        print("Updated list:", top_artists)

def main():
    # Predefined list of top ten performing artists
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", 
                   "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    
    # Display the original list
    print("Original list:", top_artists)
    
    # Call the function to replace an artist
    replace_artist(top_artists)

if __name__ == "__main__":
    # Entry point of the program
    main()
