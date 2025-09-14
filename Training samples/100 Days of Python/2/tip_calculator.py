# print("Welcome to the tip calculator")
#
# print("What was the total bill?")
#
# bill = input()
# print("$" + str(bill))
#
# print("How much tip do you like to give? 10, 12 or 15?")
# tip = input()
# print(tip)
#
# print("How many people to split the bill?")
# persons = input()
# print(persons)
#
# calculate = (float(bill) / int(persons)) * ((int(tip) / 100)+1)
# payments = round(calculate, 2)
#
# print(f"Each person should pay: ${payments}")




print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15?"))
people = int(input("How many people to split the bill?"))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")