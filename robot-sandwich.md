# Robot Instructions: Make One Cheese Sandwich

Prepared for CTI-110 with AI assistance.

## Assumptions

- The goal is one uncooked cheese sandwich made from two bread slices and one cheese slice, with no other ingredients.
- A clean, empty plate is centered on a clean table directly in front of the robot.
- Two separate, unpackaged, square bread slices lie flat to the left of the plate. The nearer slice is Bread A; the farther slice is Bread B. Each slice is 10 centimeters wide.
- One unpackaged, square cheese slice lies flat on a clean board to the right of the plate. It is 8 centimeters wide. No wrapper remains on any ingredient.
- All ingredients are ready to eat. The cheese slice stays intact when lifted by an edge.
- The robot has a clean, empty right gripper. It can identify the named objects, measure distances, and gently grip an edge without tearing or crushing food.
- The robot can move a held slice horizontally while keeping it flat. The route above the table is clear. Left and right are from the robot's viewpoint.
- Each instruction starts after the previous action has finished. Centering means aligning the horizontal center of the held slice with the horizontal center of the named target.

## Steps

1. Move the open right gripper to the nearest edge of Bread A.
2. Close the right gripper gently on that edge of Bread A.
3. Lift Bread A 10 centimeters above the table, keeping it flat.
4. Move Bread A horizontally until it is centered above the plate.
5. Lower Bread A until its bottom surface touches the plate.
6. Open the right gripper to release Bread A.
7. Raise the empty right gripper 10 centimeters above the plate.
8. Move the open right gripper to the nearest edge of the cheese slice.
9. Close the right gripper gently on that edge of the cheese slice.
10. Lift the cheese slice 10 centimeters above the board, keeping it flat.
11. Move the cheese slice horizontally until it is centered above Bread A.
12. Lower the cheese slice until its bottom surface touches Bread A.
13. Open the right gripper to release the cheese slice.
14. Raise the empty right gripper 10 centimeters above the cheese.
15. Move the open right gripper to the nearest edge of Bread B.
16. Close the right gripper gently on that edge of Bread B.
17. Lift Bread B 10 centimeters above the table, keeping it flat.
18. Move Bread B horizontally until it is centered above the cheese slice.
19. Lower Bread B until its bottom surface touches the cheese slice.
20. Open the right gripper to release Bread B.
21. Raise the empty right gripper 10 centimeters above the sandwich.
22. Stop moving.

**Done When:** The plate holds one stack in this bottom-to-top order: Bread A, the cheese slice, Bread B. The three slices are centered, the cheese lies between the bread slices, and the robot's open gripper is empty and clear of the sandwich.
