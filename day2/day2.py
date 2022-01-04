"""
Day 2 problem
"""

with open("day2_input.txt") as file: 
        lines = file.readlines()

depth = 0
horizontal = 0

for l in lines:

    l = l.replace("\n", "") # remove new line char
    command = l.split(" ")

    direction, value = command[0], int(command[1])

    if direction == 'forward':
        horizontal += value

    elif direction == 'down':
        depth += value
    
    elif direction == 'up':
        depth -= value

print(f"\nDepth:{depth} Horizontal:{horizontal}\n")
print(f"Answer: {depth*horizontal} (depth x horizontal)")

# answer == 1383564