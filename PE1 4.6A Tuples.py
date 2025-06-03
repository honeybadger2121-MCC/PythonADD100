# Create a tuple with programming class names
programming_classes = (
    'Intro to Python', 'Advanced Python', 'Database Essentials',
    'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals'
)

# Main function to print each class and count the number of courses
def main():
    for course in programming_classes:  # Loop through each item in the tuple
        print(course)
   
    print("The tuple has", len(programming_classes), "courses.")  # Print total count

# Run the program
main()