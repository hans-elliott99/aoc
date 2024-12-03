#!/usr/bin/env python3
import re
import copy

# Advent of Code 2022 [https://adventofcode.com/2022/]
# Day 5: Supply Stacks
# hans elliott



# starting stack configuration
"""
[V]     [B]                     [C]
[C]     [N] [G]         [W]     [P]
[W]     [C] [Q] [S]     [C]     [M]
[L]     [W] [B] [Z]     [F] [S] [V]
[R]     [G] [H] [F] [P] [V] [M] [T]
[M] [L] [R] [D] [L] [N] [P] [D] [W]
[F] [Q] [S] [C] [G] [G] [Z] [P] [N]
[Q] [D] [P] [L] [V] [D] [D] [C] [Z]
 1   2   3   4   5   6   7   8   9 
"""

N_STACKS = 9
STACK_HEIGHT = 8

def parse_initial_stack(lines:list[list[str]]) -> dict[list[str]]:
    """Parse stack text into a usable dict 
    """
    stacks = {i : [] for i in range(0, N_STACKS)}
    for i in range(N_STACKS):
        for j in range(0, STACK_HEIGHT): #store from top to bottom
            crate = re.sub(' +','', lines[j][i])
            crate = crate.replace('[','').replace(']','')
            if crate != '':
                stacks[i].append(crate)

    return stacks

def parse_directions(line:list[str]) -> list[int]:
    """Parse directions of the format: 'move n from i to j'
    """
    _, n, _, i, _, j = line.split(' ')
    return int(n), int(i)-1, int(j)-1


def apply_directions(stacks_:list, dirs:list, CrateMover_9001=False) -> dict[list[str]]:
    """Apply the directions to the stack, moving crates based on the CrateMover rules
    """
    stacks = copy.deepcopy(stacks_)
    # Part 2: dont reverse the order of the crates when stacking
    if CrateMover_9001: 
        for (n,frm,to) in dirs:
            stacks[to] = stacks[frm][0:n] + stacks[to]
            del stacks[frm][0:n]
    else:
    # Part 1: reverse order of the crates when stacking since "stack one at a time"
        for (n,frm,to) in dirs:
            stacks[to] = stacks[frm][0:n][::-1] + stacks[to]
            del stacks[frm][0:n]

    return stacks      

def get_top_crates(stacks:list) -> str:
    """Get final message of chars corresponding to the final top crate on each stack 
    """
    out = ""

    for i in range(N_STACKS):
        out += ''.join(stacks[i]).strip()[0]

    assert len(out) == N_STACKS
    return out




if __name__ == "__main__":

    # read input
    with open("advent-of-code/inputs/day5.txt", 'r') as f:
        
        stack_str = []
        directions = []
        count = 0
        for line in f:
            line = line.strip()
            # First, parse the stack text into row-wise lists (might be simpler to do manually)
            if count < STACK_HEIGHT:
                crates = []
                for i in range(4,N_STACKS*4+1, 4): ##each "crate" takes up 4 chars in its row
                    crates.append( line[i-4 : i-1] ) 
                stack_str.append(crates[0:STACK_HEIGHT+1])
                count +=1
            # Skip the stack index row
            elif count == STACK_HEIGHT:
                count += 1
                pass
            # The rest of the lines are the crate mover directions. Parse those into a list.
            else:
                if line != '':
                  directions.append( parse_directions(line.strip()) )

        # Parse our initial stack configuration from row-wise list to a dict of lists
        # where each list is one stack
        start_stack = parse_initial_stack(stack_str)
        # Apply the directions
        stacks1 = apply_directions(start_stack, directions)
        stacks2 = apply_directions(start_stack, directions, CrateMover_9001=True)
        

        print(f"Part 1 - Final Message: {get_top_crates(stacks1)}")
        print(f"Part 2 - Final Message: {get_top_crates(stacks2)}")