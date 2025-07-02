def main():
    # Initialize an empty list to store book titles
    book_titles = []

    # Collect 10 book titles from the user
    while len(book_titles) < 10:
        title = input("Enter a book title: ").title()  # Ensure proper capitalization
        book_titles += [title]  # Add the title to the list without using .append()

    # Create a sorted list of book titles
    books_sorted = sorted(book_titles)

    # Display the sorted book titles
    print("\nSorted Book Titles:")
    for book in books_sorted:
        print(book)

# Run the main function
if __name__ == "__main__":
    main()
# This code collects 10 book titles from the user, capitalizes them, and displays them in sorted order.
# It uses a list to store the titles and the sorted() function to sort them.