print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = input(
    "What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to slipt the bill? ")
bill_in_int = int(bill)
percentage_in_int = int(percentage) / 100 + 1
people_in_int = int(people)
total_tip = bill_in_int / people_in_int
total_tip_with_p = total_tip * percentage_in_int
total = round(total_tip_with_p, 3)
print(f"Each person should pay: ${total}")
