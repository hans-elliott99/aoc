#!/usr/bin/env python3

# Advent of Code 2022 [https://adventofcode.com/2022/]
# Day 10: Cathode-Ray Tube
# hans elliott

X = 1

# Part 1: save the x values at each of the key cycles
saveX, key_cycles = [], [20, 60, 100, 140, 180, 220]
cycle = 0

# Part 2:
# "The pixels on the CRT screen: 40 wide and 6 high
#  This CRT screen draws the top row of pixels left-to-right, then the row below that, 
#  and so on. The left-most pixel in each row is in position 0, and the right-most 
#  pixel in each row is in position 39."
# The CRT turns a pixel on if the 'sprite' is covering the pixel at the current time.
# The sprite is 3 pixels long and its center pixel is defined by X.
screen = [[0]*40 for _ in range(6)]
row, cycle2 = 0, 0



if __name__=="__main__":
    with open("advent-of-code/inputs/day10.txt") as f:
        for line in f:

            # 'addx' command takes 2 cycles and X is updated at end of second
            if line.strip().split()[0] == "addx":
                
                # PART 1 - Step through each cycle and save X value when needed
                cycle += 1
                if cycle in key_cycles:
                    saveX.append(X)      
                cycle += 1
                if cycle in key_cycles:
                    saveX.append(X)

                
                # PART 2 - Step through each cycle and turn on the corresponding
                #          pixel (at cycle-1) if the sprite covers it. Move to 
                #          the next row of the screen as needed.
                if cycle2 == 40: 
                    row += 1
                    cycle2 = 0         
                cycle2 += 1
                screen[row][cycle2-1] = 1 if cycle2-1 in [X-1, X, X+1] else 0

                if cycle2 == 40: 
                    row += 1
                    cycle2 = 0         
                cycle2 += 1
                screen[row][cycle2-1] = 1 if cycle2-1 in [X-1, X, X+1] else 0

                # SHARED - at end of 'addx', updated X
                X += int(line.strip().split()[1])
            
            # 'noop' takes 1 cycle and does nothing to X
            else: 
                # PART 1 
                cycle += 1
                if cycle in key_cycles:
                    saveX.append(X)
                
                # PART 2
                if cycle2 == 40: 
                    row += 1
                    cycle2 = 0         
                cycle2 += 1
                screen[row][cycle2-1] = 1 if cycle2-1 in [X-1, X, X+1] else 0



    # PART 1 SOLUTION - sum of the "signal strengths"
    signal_strengths = sum( key_cycles[i]*saveX[i] for i in range(len(key_cycles)) )    
    print("Part 1 - Sum of the six signal strengths:", signal_strengths)
    

    # PART 2 SOLUTION - visualize the 8 capital letters rendered on the CRT screen 
    print("\nPart 2 - Final Screen:")
    for i in range(0,6):
        [ print({1:'#', 0:'.'}[p], end=' ') for p in screen[i] ]
        print()



    #      # # # # . # . . . . # # # . . # . . . . # # # # . . # # . . # # # # . # . . . .
    #      # . . . . # . . . . # . . # . # . . . . . . . # . # . . # . . . . # . # . . . .
    #      # # # . . # . . . . # . . # . # . . . . . . # . . # . . . . . . # . . # . . . .
    #      # . . . . # . . . . # # # . . # . . . . . # . . . # . # # . . # . . . # . . . .
    #      # . . . . # . . . . # . . . . # . . . . # . . . . # . . # . # . . . . # . . . .
    #      # # # # . # # # # . # . . . . # # # # . # # # # . . # # # . # # # # . # # # # .
