#!/usr/bin/env python

# Advent of Code 2022 [https://adventofcode.com/2022/]
# Day 3: Rucksack Reorganization
# hans elliott

import sys
import string

# Each char in the file corresponds to a rucksack item-type, case matters.
# Map char to the "priority score" of the item based on the provided scoring rules.
lowercase_priotity = {c:i+1 for i,c in enumerate(string.ascii_lowercase)}
uppercase_priority = {c:i+27 for i,c in enumerate(string.ascii_uppercase)}

def score_char(char:str) -> int:
    if char in string.ascii_uppercase:
        score = uppercase_priority[char]
    else:
        score = lowercase_priotity[char]
    
    return score


# Part 1: Each line is 2 equal sized rucksacks, find the one
#         repeating char and get its priority score
def get_priority_score_part1(line: str) -> int:
    split_idx = len(line) // 2
    ruck1, ruck2 = line[:split_idx], line[split_idx:]

    repeat = set([c for c in set(ruck2) if c in set(ruck1)])                     ##use: set(ruck1) & set(ruck2)
    assert(len(repeat)==1)
    repeat = list(repeat)[0]

    return score_char(repeat)

# Part 2: Every 3 lines defines the 3 rucksacks for a group of elves.
#         Find the single item which repeats in all 3 and get priority score.
def get_priority_score_part2(group: list[str]) -> int:
    assert len(group) == 3

    repeat = set(
        [c for c in set(group[0]) if c in set(group[1]) and c in set(group[2])]   ##use: set(a) & set(b) & set(c)
    )
    assert len(repeat) == 1
    repeat = list(repeat)[0]

    return score_char(repeat)




if __name__=="__main__":

    if len(sys.argv)==1:
        file = "./advent-of-code/inputs/day3.txt"
    else:
        file = sys.argv[1]


    total_score1 = 0
    total_score2 = 0

    group = []
    with open(file, "r") as f:
        for line in f:
            group.append(line.strip())
            total_score1 += get_priority_score_part1(line.strip())

            if len(group) == 3:
                total_score2 += get_priority_score_part2(group)
                group = [] ##reset group
    

    print(f"Part 1 total score: {total_score1}")
    print(f"Part 2 total score: {total_score2}")

    