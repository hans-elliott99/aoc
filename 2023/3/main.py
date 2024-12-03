#!/usr/bin/python3.11


with open("input.txt", "r") as f:
    # add outer dots so that numbers on the edges get counted
    LINES = [f".{l}." for l in f.read().split("\n")]

N_LINES = len(LINES)


def adjacent_nums(row, col):
    part_nums = set()
    offsets = [(-1,-1), (-1,0), (-1,1),
               (0,-1), (0,1),
               (1,-1), (1,0), (1,1)]
    for y,x in offsets:
        r = row + y
        c = col + x
        if r < 0 or r >= N_LINES:
            continue
        if c < 0 or c >= len(LINES[r]):
            continue
        char = LINES[r][c]
        if char.isdigit():
            numstart = numend = c
            while LINES[r][numstart - 1].isdigit():
                numstart -= 1
            while LINES[r][numend + 1].isdigit():
                numend += 1
            part_nums.add(int(LINES[r][numstart : numend + 1]))
    return part_nums 
    

def part1():
    parts = []
    part_num_sum = 0
    for i, line in enumerate(LINES):
        for j, char in enumerate(line):
            if not char.isdigit() and char != ".":
                part_num_sum += sum(adjacent_nums(i, j))
    # sum of all part numbers (i.e., those adjacent to a symbol)
    return part_num_sum

def part2():
    # gears are "*" symbols adjacent to exactly 2 numbers
    # gear ratio = adjacent num 1 * adjacent num 2
    # we need sum of all gear ratios
    gear_ratio_sum = 0
    for i, line in enumerate(LINES):
        for j, char in enumerate(line):
            if char == "*":
                nums = adjacent_nums(i, j)
                if len(nums) == 2:
                    gear_ratio_sum += nums.pop() * nums.pop()

    return gear_ratio_sum


print(part1())
print(part2())
