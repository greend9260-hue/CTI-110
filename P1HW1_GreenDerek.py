# Derek Green
# November 1, 2026
# P1HW1 - Mathematical Expressions
# Calculate a power and an addition/subtraction expression from user input.

print("-----Calculating Exponents-----\n")
base = int(input("Enter an integer as the base value: "))
exponent = int(input("Enter an integer as the exponent: "))
result = base ** exponent
print("\n", base, "raised to the power of", exponent, "is", result, "!!")

print("\n-----Addition and Subtraction-----\n")
starting_integer = int(input("Enter a starting integer: "))
integer_to_add = int(input("Enter an integer to add: "))
integer_to_subtract = int(input("Enter an integer to subtract: "))
answer = starting_integer + integer_to_add - integer_to_subtract
print("\n", starting_integer, "+", integer_to_add, "-", integer_to_subtract,
      "is equal to", answer)
