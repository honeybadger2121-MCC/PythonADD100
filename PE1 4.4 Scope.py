# Global Constants for unit conversions
LB_TO_KG = 0.453592  # 1 lb = 0.453592 kg
IN_TO_M = 0.0254  # 1 in = 0.0254 meters

# Function to calculate BMI
def calculate_bmi(weight_lb, height_in):
    weight_kg = weight_lb * LB_TO_KG  # Convert weight to kilograms
    height_m = height_in * IN_TO_M  # Convert height to meters
    return weight_kg / (height_m ** 2)  # BMI formula

# Function to determine BMI category
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Main function to prompt user input and display results
def main():
    weight_lb = float(input("Enter your weight in pounds: "))
    height_in = float(input("Enter your height in inches: "))

    bmi = calculate_bmi(weight_lb, height_in)
    category = get_bmi_category(bmi)

    print(f"Your BMI is {bmi:.2f}, which falls into the '{category}' category.")

# Run the program
main()