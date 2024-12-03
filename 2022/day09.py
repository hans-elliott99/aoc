#!/usr/bin/env python3

# Advent of Code 2022 [https://adventofcode.com/2022/]
# Day 9: Rope Bridge
# hans elliott


x,y='x','y'
# PART 1 - Simulate a 2 segment rope, just a Head and a Tail
# PART 2 - Simulate a 10 segment rope with the same leading Head
head     = {'x':0,'y':0}
rope     = [head] + [{'x':0, 'y':0} for _ in range(9)]

# BOTH PARTS - need to track every position that the tail of interest touches
tail_positions1 = [(0,0)]
tail_positions2 = [(0,0)]


def move_head(coord:str, n:int):
    """The input file provides instructions for how to move the rope's head.
    """
    sign = int(n/abs(n))

    # Move the head one step at a time
    for i in range( abs(n) ):
        head[coord] += sign

        # Iteratively adjust the rope links based on new positions
        for i in range(1, 10):
            resolve_positions(i)
        
        # Add the new tail position to the tracking lists
        tail_positions1.append( (rope[1][x], rope[1][y]) )
        tail_positions2.append( (rope[9][x], rope[9][y]) )


def resolve_positions(rope_idx):
    
    lead = rope[rope_idx-1]
    lag = rope[rope_idx]

    lead_adj = [ # directly adjacent grid coordinates
        (lead[x],   lead[y]  ), 
        (lead[x]-1, lead[y]  ),   (lead[x]+1, lead[y]  ),
        (lead[x],   lead[y]-1),   (lead[x],   lead[y]+1)]
    lead_diag = [ # diagonally adjacent coords
        (lead[x]+1, lead[y]+1),   (lead[x]+1, lead[y]-1),
        (lead[x]-1, lead[y]-1),   (lead[x]-1, lead[y]+1) 
    ]
    
    # If the lag is not adjacent to the lead, it needs to move
    if (lag[x], lag[y]) not in lead_adj+lead_diag:
        dx = lead[x] - lag[x]
        dy = lead[y] - lag[y]

        # First identify and deal with a diagonal movement as needed
        # (add 1 to avoid div by 0 error when computing the condition)
        if (abs(dx)/(abs(dy)+1) == 1/3) | (abs(dx)/(abs(dy)+1) == 1):   
                lag[x] = lag[x]+1 if lead[x] > lag[x] else lag[x]-1
                lag[y] = lag[y]+1 if lead[y] > lag[y] else lag[y]-1

        # else, just increment whichever coordinate requires movement
        else:
            if dx != 0:
                lag[x] = lag[x]+1 if lead[x] > lag[x] else lag[x]-1
            if dy != 0:
                lag[y] = lag[y]+1 if lead[y] > lag[y] else lag[y]-1



if __name__=="__main__":
    with open("advent-of-code/inputs/day9.txt") as f:
        moves = f.read().splitlines()

    for mv in moves:
        direction, n = mv.split()
        match direction:
            case 'U':
                move_head('y',  int(n))
            case 'D':
                move_head('y', -int(n))

            case 'L':
                move_head('x', -int(n))
            case 'R':
                move_head('x',  int(n))


    print("Part 1 - Unique tail positions:  ", len(set(tail_positions1)))
    print("Part 2 - Unique tail positions:  ", len(set(tail_positions2)))