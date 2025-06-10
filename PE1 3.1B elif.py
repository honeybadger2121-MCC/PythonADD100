# This program converts a numeric grade to a letter grade using if-elif-else statements.

# Prompt the user to enter a numeric grade between 0 and 100
grade_input = input("Enter your numeric grade (0-100): ")

# Convert the input to an integer
grade = int(grade_input)

# Check if the grade is within the valid range (0 to 100)
if grade < 0 or grade > 100:
    # If the grade is not within the valid range, print an error message
    print("Error: Grade must be between 0 and 100.")
else:
    # Determine the letter grade based on standard grading scale
    if grade >= 90:
        # If the grade is 90 or above, assign letter grade 'A'
        letter_grade = 'A'
    elif grade >= 80:
        # If the grade is 80 or above but less than 90, assign letter grade 'B'
        letter_grade = 'B'
    elif grade >= 70:
        # If the grade is 70 or above but less than 80, assign letter grade 'C'
        letter_grade = 'C'
    elif grade >= 60:
        # If the grade is 60 or above but less than 70, assign letter grade 'D'
        letter_grade = 'D'
    else:
        # If the grade is less than 60, assign letter grade 'F'
        letter_grade = 'F'
    
    # Display the corresponding letter grade
    print(f"Your grade: {letter_grade}")
