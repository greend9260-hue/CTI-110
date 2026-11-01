# Derek Green
# November 1, 2026
# P4LAB1 - Turtle House
# Draw a house using a while loop and a for loop.
# Prepared with AI assistance; reviewed and tested before submission.

# Pseudocode:
# 1. Set up a light-blue window and a dark-blue drawing turtle.
# 2. Move to the lower-left corner of the house without drawing.
# 3. Use a while loop to draw the four equal sides of a square.
# 4. Move to the upper-left corner of the square without drawing.
# 5. Use a for loop to draw the three sides of a triangle above the square.
# 6. Keep the drawing window open until it is closed.

import turtle

window = turtle.Screen()
window.title("P4LAB1 - Derek Green")
window.bgcolor("lightblue")

pen = turtle.Turtle()
pen.color("navy")
pen.pensize(3)
pen.speed(5)

pen.penup()
pen.goto(-100, -120)
pen.pendown()

side = 0
while side < 4:
    pen.forward(200)
    pen.left(90)
    side = side + 1

pen.penup()
pen.goto(-100, 80)
pen.pendown()

for side in range(3):
    pen.forward(200)
    pen.left(120)

pen.hideturtle()
turtle.done()
