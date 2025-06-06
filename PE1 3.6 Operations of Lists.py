# Create a list representing seats 1 to 20
available_seats = list(range(1, 21))

while True:
    # Display available seats
    print("\nAvailable seats:")
    print(available_seats)

    # Prompt user for seat selection
    try:
        seat_input = input("Enter a seat number to purchase (or '0' to finish): ")
        # Convert input to integer
        seat_number = int(seat_input)
    except ValueError:
        print("Invalid input. Please enter a numeric seat number.")
        continue

    # Check if user wants to end the purchase process
    if seat_number == 0:
        print("Thank you for your purchases!")
        break

    # Validate seat selection
    if seat_number not in available_seats:
        if seat_number < 1 or seat_number > 20:
            print(f"Seat {seat_number} does not exist. Please choose a valid seat number.")
        else:
            print(f"Seat {seat_number} has already been sold. Please select another seat.")
        continue

    # Remove the seat from available seats
    available_seats.remove(seat_number)
    print(f"Seat {seat_number} has been successfully booked!")