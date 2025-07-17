# Define the Pet class
class Pet:
    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    # Getter and Setter for kind
    def get_kind(self):
        return self.__kind

    def set_kind(self, kind):
        self.__kind = kind

    # Getter and Setter for breed
    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

    # Getter and Setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Method to print pet details
    def print_details(self):
        print(f"Pet Name: {self.__name}")
        print(f"Kind: {self.__kind}")
        print(f"Breed: {self.__breed}")
        print("-" * 30)

# Create instances of Pet
pet1 = Pet("Dog", "Labrador", "Buddy")
pet2 = Pet("Cat", "Siamese", "Whiskers")
pet3 = Pet("Bird", "Parrot", "Kiwi")

# Call print_details for each pet
pet1.print_details()
pet2.print_details()
pet3.print_details()

# Demonstrate special methods/functions
# 1. __name__ is not directly accessible from an instance, but we can show the class name
print("Class name using __class__.__name__:", pet1.__class__.__name__)

# 2. type() shows the class used to instantiate the object
print("Type of pet2:", type(pet2))

# 3. __module__ shows the module in which the class is defined
print("Module of Pet class:", Pet.__module__)

# 4. __bases__ shows the base classes of the Pet class
print("Base classes of Pet:", Pet.__bases__)

# 5. isinstance() checks if an object is an instance of a class
print("Is pet3 an instance of Pet?", isinstance(pet3, Pet))
# 6. issubclass() checks if a class is a subclass of another class