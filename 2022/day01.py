#!/usr/bin/env python

# Advent of Code 2022 [https://adventofcode.com/2022/]
# Day 1: Calorie Counting
# hans elliott

if __name__=='__main__':

    elves = {}    ##each elf is a list of the calories they carry
    counter = 0
    calories = []
    with open("./inputs/day1.txt") as f:    
        for line in f:
            line = line.strip()
            if line == '':
                elves[counter] = calories
                # reset calories list and increment counter
                calories = []
                counter += 1
            else:
                calories.append(int(line))

    # Part 1: Get highest # of calories held by an elf 
    tot_calories = [sum(cals) for cals in elves.values()] #list of tot calories held by each elf
    assert len(elves) == len(tot_calories)

    print(f"Most calories held by any elf: {max(tot_calories)}")


    # Part 2: Get total calories of top 3 calory-carrying elves
    top3 = sorted(tot_calories, reverse=True)[:3]

    print(f"Total calories held by the top 3 elves: {sum(top3)}")