# Define the function that creates the customized song
def custom_song(animal, place, noun, adjective, number, object, person_name, verb):
    # Print the personalized song with the provided inputs
    print("\nHere's your personalized song!\n")
    print(f"Twinkle, twinkle, little {animal},")
    print(f"How I wonder what you {verb}.")
    print(f"Up above the {place} so high,")
    print(f"Like a {adjective} {noun} in the sky.")
    print(f"{number} {object} shining bright,")
    print(f"Guiding {person_name} at night.")
    print("Twinkle, twinkle, little star,")
    print("How I wonder what you are!")

# Collect user inputs for each variable
animal = input("Enter a type of animal (e.g., cat, dog): ")
place = input("Enter a place (e.g., sky, mountain): ")
noun = input("Enter a noun (singular, e.g., cloud, kite): ")
adjective = input("Enter an adjective (describes a noun, e.g., bright, shiny): ")
number = input("Enter a number: ")
object_ = input("Enter an object (e.g., star, moon): ")
person_name = input("Enter a person's name: ")
verb = input("Enter a verb (e.g., are, see, do): ")

# Call the function with the collected inputs
custom_song(animal, place, noun, adjective, number, object_, person_name, verb)
