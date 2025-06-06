# Create an empty list to store the names
names = []

# Ask the user to enter 5 names, one at a time
for i in range(5):
    name = input(f"Enter name {i + 1}: ")  # Ask for a name
    names.append(name)  # Add the name to the list

# Now we will sort the names in alphabetical order using a simple method called Bubble Sort
# Bubble Sort works by comparing two names at a time and swapping them if they are in the wrong order

# Set a flag to control the loop
swapped = True

# Keep looping until no more swaps are needed
while swapped:
    swapped = False  # Assume no swaps will happen
    # Go through the list of names
    for i in range(len(names) - 1):
        # Compare two names without worrying about uppercase/lowercase
        if names[i].lower() > names[i + 1].lower():
            # Swap the names if they are in the wrong order
            names[i], names[i + 1] = names[i + 1], names[i]
            swapped = True  # A swap happened, so we need to check again

# Print the sorted list of names
print("\nNames in alphabetical order:")
for name in names:
    print(name)

# Reverse the list so the names go from Z to A
names.reverse()

# Print the reversed list
print("\nNames in reverse alphabetical order:")
for name in names:
    print(name)
