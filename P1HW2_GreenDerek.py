# Derek Green
# November 1, 2026
# P1HW2 - Travel Expenses
# Calculate a travel budget's remaining balance after three expenses.
# Prepared with AI assistance.

# Pseudocode:
# Ask for the initial budget and travel destination.
# Ask for gas, accommodation, and food costs.
# Add the three costs to find total expenses.
# Subtract total expenses from the initial budget.
# Display the destination, budget, each expense, and remaining balance.

print("This program calculates and displays travel expenses\n")
budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
accommodation = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print("\nFuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print("\nRemaining Balance:", remaining_balance)
