print("Welcome to the tip calculator!")
#Bill
bill = float(input("What was the total bill? $"))
#Tip
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
#People
people_split = int(input("How many people to split the bill?"))
#Person formula
person_formula = float(bill*(1+(tip/100))/people_split)
#Final amount
final_amount = round(person_formula, 2)
print("Each person should pay: "+str(final_amount))
