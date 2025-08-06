# Project 2 : Tip Calculator
print("Welcome to Areeba's Coffee Planet!")

# Get user inputs
user_bill = float(input("What was the total bill? Rs "))
user_tip = int(input("How much tip do you want to give? 10, 12, or 15: "))
split_bill = int(input("How many people to split the bill? "))

# Convert tip to decimal and calculate total bill with tip
tip_percentage = user_tip / 100
total_with_tip = user_bill * (1 + tip_percentage)

# Calculate each person's share
each_person = total_with_tip / split_bill

# Display results
print(f"\nOriginal Bill: Rs {user_bill:.2f}")
print(f"Tip: {user_tip}%")
print(f"Total Bill with Tip: Rs {total_with_tip:.2f}")
print(f"Each person should pay: Rs {each_person:.2f}")
