#!/usr/bin/env python3

# Advent of Code 2022 [https://adventofcode.com/2022/]
# Day 12: Hill Climbing Algorithm
# hans elliott
import string


if __name__=="__main__":

    # Read in elevation map and convert from character to numeric values
    elevation = {c : v for (c,v) in zip(string.ascii_lowercase, range(26))}
    elevation['E'] = 26
    elevation['S'] = -1

    grid = []
    with open("advent-of-code/inputs/day12.txt") as f:
        for line in f:
            grid.append( [elevation[c] for c in line.strip()] )
    
    # Get start and end positions 
    for r, row in enumerate(grid):
        for c, x in enumerate(row):
            if x == -1:
                start_r, start_c = r, c
            if x == 26:
                end_r, end_c = r, c

    # Part 1: Breadth-first search
    ## Find shortest path from Start to End.
    ## Try every reachable node and track the distance taken to reach that node.
    q:list[tuple] = []
    q.append((0, start_r, start_c)) #distance, row, col 

    seen = {(start_r, start_c)}
    while q:
        # pop from left
        d, r, c = q.pop(0)
        # Test adjacent points: d, u, r, l
        for (nr, nc) in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]: 
            if (nr < 0) or (nc < 0) or (nr >= len(grid)) or (nc >= len(grid[0])):
                continue ##out of grid
            if (nr, nc) in seen:
                continue ##already visited
            if grid[nr][nc] - grid[r][c] > 1:
                continue ##cant jump up to this elelvation
            if nr == end_r and nc == end_c:
                print("Part 1 - distance =", d + 1)
                q.clear()
                break

            seen.add((nr, nc)) 
            # append to right
            q.append((d+1, nr, nc))

    # Part 2: Find shortest path from an elevation "a" (0) to the End marker
    ## do breadth-first search but start at end and go backwards until we reach 0
    q2:list[tuple] = []
    q2.append((0, end_r, end_c)) #distance, row, col 

    seen2 = {(end_r, end_c)}
    while q2:
        # pop from left
        d, r, c = q2.pop(0)
        # Test adjacent points: d, u, r, l
        for (nr, nc) in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]: 
            if (nr < 0) or (nc < 0) or (nr >= len(grid)) or (nc >= len(grid[0])):
                continue ##out of grid
            if (nr, nc) in seen2:
                continue ##already visited
            if grid[nr][nc] - grid[r][c] < -1:
                continue ##cant jump up to this elelvation
            if grid[nr][nc] == 0:
                print("Part 2 - distance =", d + 1)
                q2.clear()
                break

            seen2.add((nr, nc)) 
            # append to right
            q2.append((d+1, nr, nc))