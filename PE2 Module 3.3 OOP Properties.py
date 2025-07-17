class Pet:
    # Class variable
    vet_name = "Happy Tails Veterinary Clinic"

    def __init__(self, owner_first_name, owner_last_name, pet_id, pet_name, pet_type="Dog"):
        # Private instance variables
        self.__owner_first_name = owner_first_name
        self.__owner_last_name = owner_last_name
        self.__pet_id = pet_id
        self.__pet_name = pet_name
        self.__pet_type = pet_type

    # Getter and Setter for owner_first_name
    def get_owner_first_name(self):
        return self.__owner_first_name

    def set_owner_first_name(self, name):
        self.__owner_first_name = name

    # Getter and Setter for owner_last_name
    def get_owner_last_name(self):
        return self.__owner_last_name

    def set_owner_last_name(self, name):
        self.__owner_last_name = name

    # Getter and Setter for pet_id
    def get_pet_id(self):
        return self.__pet_id

    def set_pet_id(self, pet_id):
        self.__pet_id = pet_id

    # Getter and Setter for pet_name
    def get_pet_name(self):
        return self.__pet_name

    def set_pet_name(self, name):
        self.__pet_name = name

    # Getter and Setter for pet_type
    def get_pet_type(self):
        return self.__pet_type

    def set_pet_type(self, pet_type):
        self.__pet_type = pet_type

    # Method to display pet and owner information
    def display_pet_info(self):
        print(f"Owner: {self.__owner_first_name} {self.__owner_last_name}")
        print(f"Pet ID: {self.__pet_id}")
        print(f"Pet Name: {self.__pet_name}")
        print(f"Pet Type: {self.__pet_type}")
        print(f"Veterinary Office: {Pet.vet_name}")
        print("-" * 40)

# Function to check if a property exists in a pet object
def check_property(pet, property_name):
    exists = hasattr(pet, property_name)
    print(f"Property '{property_name}' exists in pet object: {exists}")
    return exists

# Create pet objects
pet1 = Pet("Alice", "Johnson", 101, "Buddy")
pet2 = Pet("Bob", "Smith", 102, "Whiskers", "Cat")
pet3 = Pet("Carol", "Davis", 103, "Goldie", "Fish")

# Use setter method to update pet2's name
pet2.set_pet_name("Shadow")

# Display pet info (2 examples)
pet1.display_pet_info()
pet2.display_pet_info()

# Check property existence (3 examples)
check_property(pet1, "_Pet__pet_name")  # True
check_property(pet2, "pet_name")        # False (not directly accessible)
check_property(pet3, "_Pet__pet_type")  # True

# Display all pet info
print("All Pets Info:")
for pet in [pet1, pet2, pet3]:
    pet.display_pet_info()
# Check if a property exists in the Pet class