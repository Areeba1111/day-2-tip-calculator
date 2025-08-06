#Project 2 : Tip Calculator
print("Welcome to the  Areeba's coffee planet")
user_bill= float(input("What was the total bill?\n"))
User_input= int(input("How much Tip do you want to give 10, 12,or 15 "))
split_bill = int(input("How many to Split the bill? "))
total_bill = (user_bill*1.12/split_bill)
print(f"Each person should pay: ${total_bill:.2f}")



