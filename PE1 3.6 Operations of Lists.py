# Create a list representing 20 seats, numbered 1 to 20
available_seats = list(range(1, 21))

while True:
    # Display the list of available seats
    print("Available seats:", available_seats)
    
    # Prompt the customer to select a seat
    seat_number = int(input("Please select a seat by entering its number (0 to end): "))
    
    if seat_number == 0:
        print("Purchase process ended.")
        break
    elif seat_number in available_seats:
        available_seats.remove(seat_number)
        print(f"Seat {seat_number} has been successfully purchased.")
    else:
        print("Invalid or already sold seat. Please try again.")
# Display the final list of available seats