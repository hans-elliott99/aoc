#!/usr/bin/env python3

# Advent of Code 2022 [https://adventofcode.com/2022/]
# Day 6: Tuning Trouble
# hans elliott

# input is one line of chars like : dvgdvvbpbtbhb....
if __name__ == "__main__":
    
    stream : str
    with open("advent-of-code/inputs/day6.txt") as f:
        stream = f.readline()

    sop_idx, mes_idx = [], []
    for i in range(0, len(stream)):
        # Part 1
        if len(set( stream[i : i+4] )) == 4:
            sop_idx.append(i+4)

        # Part 2
        if len(set( stream[i : i+14] )) == 14:
            mes_idx.append(i+14)
        
        # break once solutions are found
        if len(sop_idx)>0 & len(mes_idx)>0:
            break


    # Part 1: how many chars must be processed before the first SOP marker,
    #         which is defined as 4 consecutive unique chars
    print(f"Part 1: Start-of-Packet Marker Index:  {sop_idx[0] :>}") 

    # Part 2: how many chars must be processed before the first SOM marker,
    #         which is defined as 14 consecutive unique chars
    print(f"Part 2: Start-of-Message Marker Index: {mes_idx[0] :>}")
