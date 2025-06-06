
# Prompt the user to enter a numeric grade between 0 and 100
grade_input = input("Enter your numeric grade (0-100): ")

# Attempt to convert the input to an integer
try:
    grade = int(grade_input)
except ValueError:
    # If conversion fails (e.g., input is not a number), display an error and exit
    print("Invalid input. Please enter a number.")
    exit()

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
    print(f"Your grade: {letter_grade}")
