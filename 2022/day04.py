#!/usr/bin/env python

# Advent of Code 2022 [https://adventofcode.com/2022/]
# Day 4: Camp Cleanup
# hans elliott

def parse_ranges(line:str) -> tuple[set[int]]:
    # Parse ranges from input file
    rng1, rng2 = line.split(',')
    rng1 = [int(i) for i in rng1.split("-")]
    rng2 = [int(i) for i in rng2.split("-")]

    # +1 since range returns start:end-1
    r1 = set([ i for i in range(rng1[0], rng1[1]+1) ])
    r2 = set([ i for i in range(rng2[0], rng2[1]+1) ])

    return r1, r2

# Part 1: Count pair instances where one range fully contains the other
def det_full_containment(line:str) -> bool:

    # Parse ranges
    r1, r2 = parse_ranges(line)

    # Set logic: if range1 or range2 are a subset of the other,
    #            then one range fully contains the other.
    if (r1 <= r2) | (r2 <= r1):
        return True
    else:
        return False

# Part 2: Count pair instances where ranges overlap
def det_overlap(line:str) -> bool:
    # Parse ranges
    r1, r2 = parse_ranges(line)

    # Set logic: check for any intersection between ranges
    if len(r1&r2) > 0:
        return True
    else:
        return False



if __name__=="__main__":
    
    sum_part1 = 0
    sum_part2 = 0
    with open("advent-of-code/inputs/day4.txt") as f:
        for line in f:
            sum_part1 += det_full_containment(line.strip())
            sum_part2 += det_overlap(line.strip())

    print(f"Part 1 - Total: {sum_part1}")
    print(f"Part 2 - Total: {sum_part2}")