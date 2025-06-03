housing = float(input("Enter your monthly rent or mortgage: "))
utilities = float(input("Enter your monthly utilities bill: "))
groceries = float(input("Enter your monthly groceries bill: "))
transport = float(input("Enter your monthly transportation bill: "))
health_Care = float(input("Enter your monthly health care bill: "))
personal_Care = float(input("Enter your monthly personal care bill: "))
clothing = float(input("Enter your monthly clothing bill: "))
debt = float(input("Enter your monthly debt outside of what you've already listed: "))
budget = float(input("Enter your monthly budget: "))
#the above collects information from the user to use to provide them with the percent of each catagory to their budget

housingPercent = housing / Budget *100
# divides housing amount by the budget 
utilitiesPercent = utilities / Budget *100
# divides utilites amount by the budget
groceriesPercent = groceries / Budget *100
# divides groceries amount by the budget
transportPercent = transport / Budget *100
# divides transportation amount by the budget
health_CarePercent = health_Care / Budget *100
# divides health care amount by the budget
personal_CarePercent = personal_Care / Budget *100
# divides personal care amount by the budget
clothingPercent = clothing / Budget *100
# divides clothing amount by the budget
debtPercent = debt / Budget *100
# divides debt amount by the budget
grandDebtTotal = housing + utilities + groceries + transport + health_Care + personal_Care + clothing + debt
# adds all the monthly bills together for the total monthly debt
grandTotal = Budget - grandDebtTotal
#subtracts the budget from the monthly debt to get the remaining amount of money for the month

print(f"The percentage of your rent or mortgage to your monthly budget is {housingPercent:.2f}%")
print(f"The percentage of your Utilities Bills to your monthly budget is {utilitiesPercent:.2f}%")
print(f"The percentage of your Groceries Bills to your monthly budget is {groceriesPercent:.2f}%")
print(f"The percentage of your Transportation Bills to your monthly budget is {transportPercent:.2f}%")
print(f"The percentage of your Health Care Bills to your monthly budget is {health_CarePercent:.2f}%")
print(f"The percentage of your Personal Care Bills to your monthly budget is {personal_CarePercent:.2f}%")
print(f"The percentage of your Clothing Bills to your monthly budget is cClothingPercent:.2f}%")
print(f"The percentage of your Debt to your monthly budget is {debtPercent:.2f}%")
print(f"The total amount of money spent for the month is {grandDebtTotal:.2f} dollars")
print(f"The total amount of money you have left for the month is {grandTotal:.2f} dollars")
# displays the results ^^^^
