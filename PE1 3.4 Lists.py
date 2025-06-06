# Create a list containing the names of the days of the week
# This will be used to prompt the user for input for each day
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Initialize an empty list to store the number of steps taken each day
steps = []

# Loop through each day in the 'days' list
for day in days:
    # Ask the user to enter the number of steps taken on the current day
    # Convert the input from string to integer
    steps_taken = int(input(f"Enter the number of steps taken on {day}: "))
    
    # Add the entered number of steps to the 'steps' list
    steps.append(steps_taken)

# Print a blank line and a heading for the step summary
print("\nSteps taken each day:")

# Loop through the indices of the 'days' list
# This allows us to access both the day and the corresponding steps using the same index
for i in range(len(days)):
    # Print the day and the number of steps taken on that day
    print(f"{days[i]}: {steps[i]} steps")

# Calculate the total number of steps taken during the week using the sum() function
total_steps = sum(steps)
# Display the total steps
print(f"\nTotal steps in the week: {total_steps}")

# Calculate the average number of steps per day
# Divide the total steps by the number of days (length of the steps list)
average_steps = total_steps / len(steps)
# Display the average steps, formatted to 2 decimal places
print(f"Average steps per day: {average_steps:.2f}")
