#!/usr/bin/env python3

# Advent of Code 2022 [https://adventofcode.com/2022/]
# Day 14: Regolith Reservoir
# hans elliott

sand_start = (500,0)

# Sand falls one unit at a time. Each unit tries falling down and if blocked it tries down-left,
# and then down-right. If all are blocked, it settles.

def settle_sand_unit_p1(rocks:set, sand:set) -> tuple[int,int | None]:
    """Determine the resting position of the next sand unit. If all positions
    are filled, return empty tuple.
    For part 1: there is not floor, so we stop when sand starts falling into the
    infinite abyss (ie, below the 'bottom' rock).
    """
    bottom = max([y for x,y in rocks]) ##lowest rock(s)
    sand_pos = (500,0)

    blocked = rocks.union(sand)
    while True:
        down = (sand_pos[0], sand_pos[1]+1)
        down_left = (sand_pos[0]-1, sand_pos[1]+1)
        down_right = (sand_pos[0]+1, sand_pos[1]+1)

        if (down in blocked) and (down_left in blocked) and (down_right in blocked):
            break 
        if (down not in blocked):
            sand_pos = down
            if sand_pos[1] == bottom:
                sand_pos = ()
                break
        elif (down in blocked) and (down_left not in blocked):
            sand_pos = down_left
            if sand_pos[1] == bottom:
                sand_pos = ()
                break
        elif (down in blocked) and (down_left in blocked) and (down_right not in blocked):
            sand_pos = down_right
            if sand_pos[1] == bottom:
                sand_pos = ()
                break

    return sand_pos

def settle_sand_unit_p2(rocks:set, sand:set) -> tuple[int,int | None]:
    """Determine the resting position of the next sand unit. If all positions
    are filled, return empty tuple.
    For part 2: there is a floor 2 positions below the lowest rock (expanding infintely out),
    so we stop when sand has filled to the starting point (500, 0).
    """
    bottom = max([y for x,y in rocks]) + 2 ##floor
    sand_pos = (500,0)

    blocked = rocks.union(sand)
    while True:
        down = (sand_pos[0], sand_pos[1]+1)
        down_left = (sand_pos[0]-1, sand_pos[1]+1)
        down_right = (sand_pos[0]+1, sand_pos[1]+1)
        floor = [(sand_pos[0], bottom), (sand_pos[0]-1, bottom), (sand_pos[0]+1, bottom)]
        for f in floor:
            blocked.add(f)

        if (down in blocked) and (down_left in blocked) and (down_right in blocked):
            if sand_pos == (500, 0):
                sand_pos = ()
            break 
        if (down not in blocked):
            sand_pos = down
        elif (down in blocked) and (down_left not in blocked):
            sand_pos = down_left
        elif (down in blocked) and (down_left in blocked) and (down_right not in blocked):
            sand_pos = down_right

    return sand_pos


def draw_grid(rocks:set, sand:set, floor_bonus:int=0):
    """Visualize the result.
    """
    blocked = rocks.union(sand)
    max_x = max([x for x,y in blocked])
    min_x = min([x for x,y in blocked])
    max_y = max([y for x,y in rocks]) + floor_bonus 
    min_y = 0

    rows = []
    for r in range(min_y, max_y+1):
        out = ""
        for c in range(min_x, max_x+1):
            if (c,r) in rocks:
                out += "#"
            elif (c,r) in sand:
                out += "o"
            elif (c,r) == (500,0): ##sand start pos
                out += "s"
            elif r == max_y:
                out += "~" ##floor
            else:
                out += "." ##air
        rows.append(out)
    return rows


if __name__=="__main__":

    # Parse input
    inputs = []
    ys = []
    with open("advent-of-code/inputs/day14.txt") as f:
        l = []
        for line in f:
            coords = line.strip().split("->")
            for c in coords:
                x,y = c.split(',')
                l.append( (int(x.strip()), int(y.strip())) )
                ys.append(int(y))
            inputs.append( l )    
            l = []

    # Get the set of positions which contain rocks
    rocks = set()
    for vec in inputs:
        for i in range(len(vec)-1):
            dx = vec[i+1][0] - vec[i][0]
            dy = vec[i+1][1] - vec[i][1]
            if dx != 0:
                sign = int(dx/abs(dx))
                for n in range(abs(dx)+1):
                    rocks.add( (vec[i][0]+(sign*n), vec[i][1]) )
            else:
                sign = int(dy/abs(dy))
                for n in range(abs(dy)+1):
                    rocks.add( (vec[i][0], vec[i][1]+(sign*n)) )

    # part 1
    sand = set()
    while True:
        new_sand = settle_sand_unit_p1(rocks, sand)
        if new_sand:
            sand.add(new_sand)
        else:
            break
    print("Part 1: Number of sand units", len(sand))

    rows = draw_grid(rocks,sand)
    for row in rows:
        print(row)



    # part 2
    sand2 = set()
    while True:
        new_sand = settle_sand_unit_p2(rocks, sand2)
        if new_sand:
            sand2.add(new_sand)
        else:
            sand2.add((500,0))
            break
    print("Part 2: Number of sand units", len(sand2))

    rows = draw_grid(rocks, sand2, floor_bonus=2)
    with open("advent-of-code/outputs/day14viz.txt", "w") as f:
        for row in rows:
            f.write(row+'\n')

