# Define the list of time slots
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

# Initialize an empty list to store heart rates
heart_rates = []

# Loop through each time slot to get user input
for time in time_slots:
    hr = int(input(f"Enter your heart rate (in BPM) during {time}: "))
    # Optional: Validate the input if desired
    while hr < 30 or hr > 220:
        correct = input(f"The value {hr} is outside typical human heart rates. Are you sure? (Y/N): ")
        if correct.lower() == 'y':
            break
        else:
            hr = int(input(f"Please re-enter your heart rate during {time}: "))
    # Append the time and heart rate as a list inside the main list
    heart_rates.append([time, hr])

# Calculate the average heart rate
total_hr = 0
for entry in heart_rates:
    total_hr += entry[1]
average_hr = total_hr / len(heart_rates)

# Display the times and heart rates
print("\nYour heart rates:")
for entry in heart_rates:
    print(f"During {entry[0]}, your heart rate was {entry[1]} BPM.")

# Display the average heart rate
print(f"\nYour average heart rate for the day is: {average_hr:.2f} BPM.")