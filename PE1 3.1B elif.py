# Define a function to convert numeric grade to letter grade
# Get the numeric grade from the user
grade = int(input("Enter your numeric grade (0-100): "))

# Check if the grade is within the valid range (0 to 100)
if grade < 0 or grade > 100:
    print("Error: Grade must be between 0 and 100.")
else:
    # Determine the letter grade based on standard grading scale
    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'
    elif grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    # Display the corresponding letter grade
    print("Your grade: ", letter_grade)
