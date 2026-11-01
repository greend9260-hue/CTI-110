# Derek Green
# November 1, 2026
# P4LAB2 - Multiplication Tables
# Display multiplication tables and allow the user to run again.
# Prepared with AI assistance.

# Pseudocode:
# Set the repeat answer to yes.
# While the answer is yes, ask for an integer.
# If the integer is nonnegative, use a for loop for multipliers 1 through 12.
# Otherwise, explain that negative values are not accepted.
# Ask whether to run again; require yes or no.
# End when the answer is no.

print("P4LAB2 - Derek Green")
run_again = "yes"
while run_again == "yes":
    number = int(input("Enter an integer: "))
    if number >= 0:
        for multiplier in range(1, 13):
            print(f"{number} * {multiplier} = {number * multiplier}")
    else:
        print("Negative values are not accepted.")

    run_again = input("Would you like to run the program again? (yes/no): ")
    while run_again != "yes" and run_again != "no":
        run_again = input("Please enter yes or no: ")
    print()

print("Exiting program...")
