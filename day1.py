############################################# Part 1 ###############################################

with open('day1_input.txt') as f:
    lines = f.readlines()

counter = 0
i = 1
while (i < len(lines)):
    if (int(lines[i]) > int(lines[i-1])): # check if if current number is bigger than previous
        counter += 1
        # print(f"{int(lines[i])} > {int(lines[i-1])}")
    i += 1

print(f"PART1: Total measurement increases: {counter}\n")

###################################################################################################

############################################# Part 2 ###############################################


