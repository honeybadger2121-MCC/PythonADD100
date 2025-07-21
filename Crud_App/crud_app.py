# Display the main menu and get the user's choice
def main_menu():
    print("Menu:")
    choice = 0
    # Loop until a valid choice is entered
    while not(1 <= choice <= 5):
        try:
            print("\n\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")

# Main loop that keeps the program running until the user chooses to quit
def main():
    choice = 0
    while choice != 5:
        choice = main_menu()
        if choice == 1:
            create()
        elif choice == 2:
            read()
        elif choice == 3:
            update()
        elif choice == 4:
            delete()
    print("\nData saved as customer_list.txt\n")

# Check if the customer list file exists and read its contents
def check():
    try:
        file = open("customer_list.txt", 'r')
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return []

# Save the updated customer list back to the file
def save(output):
    file = open("customer_list.txt", 'w')
    for line in output:
        file.write(line)
    file.close()
    print("File updated.")

# Create a new customer entry and append it to the list
def create():
    customer = check()
    fname = input("Please enter the customer's first name: ")
    lname = input("Please enter the customer's last name: ")
    phone = input("Please enter the customer's phone: ")
    email = input("Please enter the customer's email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\n"
    customer.append(entry)
    save(customer)

# Read and display entries that match a given last name
def read():
    customer = check()
    lname = input("Enter the last name to search for: ")
    found = False
    for entry in customer:
        if lname.lower() in entry.lower():
            print(entry.strip())
            found = True
    if not found:
        print("No entry found with that last name.")

# Update an existing entry by searching for the last name
def update():
    customer = check()
    lname = input("Enter the last name of the entry to update: ")
    updated = False
    for i in range(len(customer)):
        if lname.lower() in customer[i].lower():
            print(f"Current entry: {customer[i].strip()}")
            fname = input("New first name: ")
            lname = input("New last name: ")
            phone = input("New phone: ")
            email = input("New email: ")
            customer[i] = f"{fname}, {lname}, {phone}, {email}\n"
            updated = True
            break
    if updated:
        save(customer)
    else:
        print("No entry found to update.")

# Delete an entry by last name
def delete():
    customer = check()
    lname = input("Enter the last name of the entry to delete: ")
    # Create a new list excluding entries that match the last name
    new_list = [entry for entry in customer if lname.lower() not in entry.lower()]
    if len(new_list) != len(customer):
        save(new_list)
        print("Entry deleted.")
    else:
        print("No entry found to delete.")

# Start the program
if __name__ == "__main__":
    main()
# crud_app.py
# A simple CRUD application for managing customer email entries.
# It allows users to create, read, update, and delete entries stored in a text file.
# The application provides a menu-driven interface for user interaction.
# The customer entries are stored in a file named 'customer_list.txt'.
# The program checks for the existence of this file and creates it if it does not exist.