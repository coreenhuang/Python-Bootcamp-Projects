#Calculating bill with tips per person

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))

percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")

multiplier = int(percentage_tip) / 100 + 1

number_of_people = int(input("How many people to split the bill? "))

bill_per_person = total_bill * multiplier / number_of_people

print(f"Each person should pay: ${bill_per_person:.2f}")