Housing = float(input("Enter your monthly rent or mortgage: "))
Utilities = float(input("Enter your monthly utilities bill: "))
Groceries = float(input("Enter your monthly groceries bill: "))
Transport = float(input("Enter your monthly transportation bill: "))
Health_Care = float(input("Enter your monthly health care bill: "))
Personal_Care = float(input("Enter your monthly personal care bill: "))
Clothing = float(input("Enter your monthly clothing bill: "))
Debt = float(input("Enter your monthly debt outside of what you've already listed: "))
Budget = float(input("Enter your monthly budget: "))
#the above collects information from the user to use to provide them with the percent of each catagory to their budget

HousingPercent = Housing / Budget 
# divides housing amount by the budget
UtilitiesPercent = Utilities / Budget
# divides utilites amount by the budget
GroceriesPercent = Groceries / Budget
# divides groceries amount by the budget
TransportPercent = Transport / Budget
# divides transportation amount by the budget
Health_CarePercent = Health_Care / Budget
# divides health care amount by the budget
Personal_CarePercent = Personal_Care / Budget
# divides personal care amount by the budget
ClothingPercent = Clothing / Budget
# divides clothing amount by the budget
DebtPercent = Debt / Budget
# divides debt amount by the budget
grandDebtTotal = Housing + Utilities + Groceries + Transport + Health_Care + Personal_Care + Clothing + Debt
# adds all the monthly bills together for the total monthly debt
grandTotal = Budget - grandDebtTotal
#subtracts the budget from the monthly debt to get the remaining amount of money for the month

print(f"The percentage of your rent or mortgage to your monthly budget is {HousingPercent:.2f}%")
print(f"The percentage of your Utilities Bills to your monthly budget is {UtilitiesPercent:.2f}%")
print(f"The percentage of your Groceries Bills to your monthly budget is {GroceriesPercent:.2f}%")
print(f"The percentage of your Transportation Bills to your monthly budget is {TransportPercent:.2f}%")
print(f"The percentage of your Health Care Bills to your monthly budget is {Health_CarePercent:.2f}%")
print(f"The percentage of your Personal Care Bills to your monthly budget is {Personal_CarePercent:.2f}%")
print(f"The percentage of your Clothing Bills to your monthly budget is {ClothingPercent:.2f}%")
print(f"The percentage of your Debt to your monthly budget is {DebtPercent:.2f}%")
print(f"The total amount of money spent for the month is {grandDebtTotal:.2f} dollars")
print(f"The total amount of money you have left for the month is {grandTotal:.2f} dollars")
# displays the results ^^^^