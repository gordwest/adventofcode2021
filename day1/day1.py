
### Part 1 ###
def part1(lines_arr):
        counter = 0
        idx = 1
        while idx < len(lines_arr):
            if (int(lines_arr[idx]) > int(lines_arr[idx-1])):
                counter += 1
                # print(f"{int(lines_arr[idx])} is greater than {int(lines_arr[idx-1])}")
            idx += 1
        print(f"\nThere are {counter} increases!")

def part2(lines):
    windows = []
    outer_idx = 0
    while outer_idx < len(lines)-2:
        window_sum = 0
        for i in range(0,3):
            window_sum += int(lines[outer_idx + i])
        windows.append(window_sum)
        outer_idx += 1

    # print(windows)
    part1(windows)


if __name__ == "__main__":

    with open("day1_input.txt") as file: 
        lines = file.readlines()

    part1(lines)
    part2(lines)