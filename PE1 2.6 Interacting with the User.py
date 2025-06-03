# Collects information from the user about their monthly expenses and budget
housing = float(input("Enter your monthly rent or mortgage: "))
utilities = float(input("Enter your monthly utilities bill: "))
groceries = float(input("Enter your monthly groceries bill: "))
transport = float(input("Enter your monthly transportation bill: "))
health_Care = float(input("Enter your monthly health care bill: "))
personal_Care = float(input("Enter your monthly personal care bill: "))
clothing = float(input("Enter your monthly clothing bill: "))
debt = float(input("Enter your monthly debt outside of what you've already listed: "))
budget = float(input("Enter your monthly budget: "))

# Calculates the percentage of each expense category relative to the budget
housingPercent = housing / budget * 100
# Percentage of housing cost
utilitiesPercent = utilities / budget * 100
# Percentage of utilities cost
groceriesPercent = groceries / budget * 100
# Percentage of groceries cost
transportPercent = transport / budget * 100
# Percentage of transportation cost
health_CarePercent = health_Care / budget * 100
# Percentage of health care cost
personal_CarePercent = personal_Care / budget * 100
# Percentage of personal care cost
clothingPercent = clothing / budget * 100
# Percentage of clothing cost
debtPercent = debt / budget * 100
# Percentage of additional debt

# Calculates the total monthly expenses and the remaining budget
grandDebtTotal = housing + utilities + groceries + transport + health_Care + personal_Care + clothing + debt
# Total monthly expenses
grandTotal = budget - grandDebtTotal
# Remaining budget after expenses

# Displays the results to the user
print(f"The percentage of your rent or mortgage to your monthly budget is {housingPercent:.2f}%")
print(f"The percentage of your Utilities Bills to your monthly budget is {utilitiesPercent:.2f}%")
print(f"The percentage of your Groceries Bills to your monthly budget is {groceriesPercent:.2f}%")
print(f"The percentage of your Transportation Bills to your monthly budget is {transportPercent:.2f}%")
print(f"The percentage of your Health Care Bills to your monthly budget is {health_CarePercent:.2f}%")
print(f"The percentage of your Personal Care Bills to your monthly budget is {personal_CarePercent:.2f}%")
print(f"The percentage of your Clothing Bills to your monthly budget is {clothingPercent:.2f}%")
print(f"The percentage of your Debt to your monthly budget is {debtPercent:.2f}%")
print(f"The total amount of money spent for the month is {grandDebtTotal:.2f} dollars")
print(f"The total amount of money you have left for the month is {grandTotal:.2f} dollars")
