# Derek Green
# November 1, 2026
# P4HW1 - Scores and Letter Grade
# Collect valid scores, drop the lowest, and calculate an average and grade.
# Newly prepared with AI assistance; no earlier source file was available.

# Pseudocode:
# Ask for the number of scores; require at least two so one can be dropped.
# Create an empty score list.
# For each requested score, ask for a score and repeat while outside 0 to 100.
# Add each valid score to the list.
# Find and remove one occurrence of the lowest score.
# Calculate the average of the remaining scores.
# Use the average to select A, B, C, D, or F.
# Display the lowest score, modified list, average, and letter grade.

print("P4HW1 - Derek Green")
score_count = int(input("How many scores do you want to enter? "))
while score_count < 2:
    print("Enter at least two scores so the lowest score can be dropped.")
    score_count = int(input("How many scores do you want to enter? "))

score_list = []
for score_number in range(1, score_count + 1):
    score = float(input(f"Enter score #{score_number}: "))
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{score_number} again: "))
    score_list.append(score)

lowest_score = min(score_list)
score_list.remove(lowest_score)
average = sum(score_list) / len(score_list)

if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print("\n--------------Results--------------")
print(f"{'Lowest Score:':<20}{lowest_score}")
print(f"{'Modified List:':<20}{score_list}")
print(f"{'Scores Average:':<20}{average:.2f}")
print(f"{'Grade:':<20}{letter_grade}")
print("-----------------------------------")
