# Day 3

with open("day3_input_subset.txt") as file: 
    lines = file.readlines()

# get stats
length = len(str(lines[0])) -1

occurences = []
for i in range(length):
    occurences.append(0)

for binStr in lines: # find bit occurences from input
    i = 0
    while i < length:
        if binStr[i] == '0':
            occurences[i] -= 1
        elif binStr[i] == '1':
            occurences[i] += 1

        i += 1
print(occurences)

gamma_rate = ''
epsilon_rate = '0b'
for s in occurences:
    if s < 0:
        g_bit = 0
        e_bit = 1
    elif s > 0:
        g_bit = 1
        e_bit = 0
    gamma_rate = gamma_rate + str(g_bit)
    epsilon_rate = epsilon_rate + str(e_bit)

print(f'Gamma Rate: {gamma_rate}')
print(f'Epsilon Rate: {epsilon_rate}')

print(int(gamma_rate))

